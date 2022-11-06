"""30 Day Map Challenge | Day 06: Networks (this was actual hell)

I first wanted to compare "metro network length" to "city area"
but found out that plotting water bodies for cities I was interested
in with OSMnx isn't trivial so I've switched over to look at the
destinations in Europe of Turkish Airlines flights from Istanbul. 
Just to find out that that's not as trivial as well.
"""

import osmnx as ox
import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
from keplergl import KeplerGl

# Destination data from 
# https://www.flightconnections.com/flights-from-istanbul-ist
df = pd.read_csv("Day06/data/destinations.txt")

ist = ox.geocode_to_gdf("Istanbul").centroid[0]

for place in df["FlightDestinations"].items():
    with open("Day06/data/linestrings.csv", "a") as csv:
        csv.write(
            f"{place[1]};{LineString([ist, ox.geocode_to_gdf(place[1]).centroid[0]])};{ist.y};{ist.x};{ox.geocode_to_gdf(place[1]).centroid[0].y};{ox.geocode_to_gdf(place[1]).centroid[0].x}\n"
        )
        csv.close()

df_linestrings = pd.read_csv("Day06/data/linestrings.csv", sep=";")
gdf_linestrings = gpd.GeoDataFrame(df_linestrings, geometry=gpd.GeoSeries.from_wkt(df_linestrings["linestring"]))

map = KeplerGl()
map.add_data(data=gdf_linestrings, name="Linestrings")
map.save_to_html(file_name = "Day06/Day06_Networks.html")
