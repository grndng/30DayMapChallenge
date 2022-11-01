"""30 Day Map Challenge | Day 02: Lines (looking at postcodes)

Inspired by the US ZIPScribble Map, I've looked for a way
to replicate the same process to Germany. Mainly I wanted 
to see if regions will be as neatly divideable by ZIP codes
in Germany as well.
"""

import pandas as pd
import altair as alt
import geopandas as gpd

# Loading post codes (PLZ = Postleitzahl = German for "postcode")
plz = pd.read_csv("Day02/data/PLZ.csv", names=["postcode", "cityname", "lon", "lat"], header=None, delimiter=";") # https://launix.de/launix/launix-gibt-plz-datenbank-frei/

# Some regions in Germany have postcodes starting with a 0
# which was not included in my dataset so I decided to add
# the zero now to have an easier life later.
for i in plz["postcode"]:
    if len(str(i)) < 5:
        plz["postcode"] = plz["postcode"].astype(str).str.pad(width=5, side="left", fillchar="0")

# Loading the federal states of Germany to later use as base
# map to see how the postcodes compare to the state borders
de = gpd.read_file("Day02/data/bl.json")

# Loading the basemap as altair chart
basemap = alt.Chart(de).mark_geoshape(
        fill = "lightgray",
        stroke = "white",
        opacity= 0.2
    ).properties(
        width=1400,
        height=1000
    )

# Loading the lines and points to create visualization
# I'm adding points for the *.html mainly so the tooltips
# can be hovered over more easily
# from https://nextjournal.com/sdanisch/cartographic-visualization
# and https://altair-viz.github.io/altair-tutorial/notebooks/09-Geographic-plots.html
postcode_lines = alt.Chart(plz).transform_filter(
    "-10 < datum.lon && 25 < datum.lat && datum.lat < 60"
    ).transform_calculate(
        "Leading Digit", alt.expr.substring(alt.datum.postcode, 0, 1)
    ).mark_line(
        strokeWidth=1
    ).encode(
        longitude="lon:Q", # Q for quantitative (continuous real-valued quantity)
        latitude="lat:Q", 
        color="Leading Digit:N", # N for nominal (discrete unordered category)
        tooltip=["postcode", "cityname", "lat", "lon"]
    ).properties(
        width=1400,
        height=1000
    )

postcode_pts = alt.Chart(plz).transform_calculate(
    "Leading Digit", alt.expr.substring(alt.datum.postcode, 0, 1)
    ).mark_circle(
        size=10, opacity=0.5
    ).encode(
        longitude="lon:Q", # Q for quantitative (continuous real-valued quantity)
        latitude="lat:Q", 
        color="Leading Digit:N", # N for nominal (discrete unordered category)
        tooltip=["postcode", "cityname", "lat", "lon"]
    ).properties(
        width=1400,
        height=1000
    )

# Putting together basemap, lines and points
base_and_lines = alt.layer(basemap, postcode_lines).configure_view(
    stroke="transparent"
)

with_points = alt.layer(basemap, postcode_lines, postcode_pts).configure_view(
    stroke="transparent"
)

postcode_lines = alt.layer(postcode_lines).configure_view(
    stroke="transparent"
)

# Saving them as html files
base_and_lines.save("Day02/Day02_Lines.html")
postcode_lines.save("Day02/Day02_Lines_only.html")
with_points.save("Day02/Day02_with_points.html")