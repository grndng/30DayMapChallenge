"""30DayMapChallenge | Day 11: Red

Most of the time things that aren't optimal will be
visualised in red and today we're following that trend
by taking a look at the deforestation on our planet.
"""

import osmnx as ox
import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl

df = gpd.read_file("Day11/data/annual-change-forest-area.csv")

# 5 year difference to 2010 so we need
# data only for 2015 (data type is str...)
df = df.loc[df["Year"] == str(2015)]

# Changing data type for the annual net change of
# forest areas to float for further use
df["AnnualNetChangeinHA"] = df["AnnualNetChangeinHA"].astype(float)

# There is an Entity in the dataset called "world"
# and since we're not looking at the worlds average,
# we can simply go ahead and get rid of it and also 
# of the values in annual net change above 0 since we
# are only interested in areas with less forest in comparison
df.drop(df.loc[df["Entity"]=="World"].index, inplace=True) 
df.drop(df.loc[df["AnnualNetChangeinHA"]>=0].index, inplace=True)

world_json = gpd.read_file("Day11/data/world.json")
world_json = world_json.rename(columns = {"name_en":"Entity"})
df_with_geometries = pd.merge(df,world_json[["Entity","geometry"]], on="Entity", how="left")

gdf_w_geoms = gpd.GeoDataFrame(df_with_geometries.drop(columns='geometry_x'), geometry="geometry_y")
gdf_w_geoms = gdf_w_geoms.rename(columns = {"geometry_y":"geometry"})
gdf_w_geoms = gdf_w_geoms.dropna() # some countries don't have a geometry :[

map = KeplerGl()
map.add_data(data=gdf_w_geoms, name="Countries w negative Net Change")
map.save_to_html(file_name = "Day11/Day11_Red.html")