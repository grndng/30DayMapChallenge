"""30 Day Map Challenge | Day 02: Lines (looking at postcodes)

Inspired by the US ZIPScribble Map, I've looked for a way
to replicate the same process to Germany. Mainly I wanted 
to see if regions will be as neatly divideable by ZIP codes
in Germany as well.
"""

import pandas as pd
import altair as alt
import geopandas as gpd

# Loading Dataframe
zipcodes = pd.read_csv("Day02/data/PLZ.csv", names=["postcode", "cityname", "lon", "lat"], header=None, delimiter=";") # https://launix.de/launix/launix-gibt-plz-datenbank-frei/

# adding leading zeroes to postcodes from 
for i in zipcodes["postcode"]:
    if len(str(i)) < 5:
        zipcodes["postcode"] = zipcodes["postcode"].astype(str).str.pad(width=5, side="left", fillchar="0")

de = gpd.read_file("Day02/data/bl.json")

basemap = alt.Chart(de).mark_geoshape(
    fill = "lightgray",
    stroke = "white"
).properties(
    width=1000,
    height=800
)

# from https://nextjournal.com/sdanisch/cartographic-visualization
# and https://altair-viz.github.io/altair-tutorial/notebooks/09-Geographic-plots.html

postcode_lines = alt.Chart(zipcodes).transform_filter(
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
    width=1000,
    height=800
)

pts = alt.Chart(zipcodes).transform_calculate(
    "Leading Digit", alt.expr.substring(alt.datum.postcode, 0, 1)
).mark_square(
    size=2, opacity=0.5
).encode(
    longitude="lon:Q", # Q for quantitative (continuous real-valued quantity)
    latitude="lat:Q", 
    color="Leading Digit:N", # N for nominal (discrete unordered category)
    tooltip=["postcode", "cityname", "lat", "lon"]
)


base_and_lines = basemap + postcode_lines
base_and_lines = base_and_lines + pts
base_and_lines.save("Day02/Day02_Lines.html")
postcode_lines.save("Day02/Day02_Lines_only.html")