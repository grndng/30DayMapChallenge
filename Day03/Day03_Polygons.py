"""30 Day Map Challenge | Day 03: Polygons (Gender Pay Gap)

I've read an article about the gender pay gap and how
it is still a problem in most places. I've first taken
a look at data in Germany but thought that maybe stepping
back and taking a look at Europe would make sense, too.
"""

import geopandas as gpd
import pandas as pd
from keplergl import KeplerGl


gpg_df = pd.read_csv("./Day03/data/gender_pay_gap_eurostat.csv")
eu_df = gpd.read_file("./Day03/data/europe.json")

# I'm renaming for ease of use later on and also for merging over "name_long" in a minute
gpg_df.rename(columns={"geo":"name_long", "TIME_PERIOD":"year", "OBS_VALUE":"gap"}, inplace=True)

merged_df  = eu_df.merge(gpg_df, on="name_long", how="left")
merged_gdf = gpd.GeoDataFrame(merged_df)

# I'm filtering the data by 2020 since that's what I want to look at
filter_2020 = merged_gdf["year"] == 2020
merged_gdf = merged_gdf.loc[filter_2020]

mean_gap = merged_gdf["gap"].mean()

"""
# I've intended to use the difference to the mean gender pay gap
# over the dataset but totally forgot about it when creating the map...
for _, i in merged_gdf["gap"].items():
    print(mean_gap-i)
"""

map = KeplerGl()
map.add_data(data=merged_gdf, name="GDF")
map.save_to_html(file_name = "Day03_Polygons.html")
