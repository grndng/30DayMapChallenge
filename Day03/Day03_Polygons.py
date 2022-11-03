"""30 Day Map Challenge | Day 03: Polygons (Gender Pay Gap)

I've read an article about the gender pay gap and how
it is still a problem in most places. I've first taken
a look at data in Germany but thought that maybe stepping
back and taking a look at Europe would make sense, too.
"""

import geopandas as gpd
import pandas as pd
from keplergl import KeplerGl

# NUR 2020 nehmen!

gpg_df = pd.read_csv("./Day03/data/gender_pay_gap_eurostat.csv")
eu_df = gpd.read_file("./Day03/data/europe.json")

gpg_df.rename(columns = {"geo":"name_long", "TIME_PERIOD":"year", "OBS_VALUE":"gap"}, inplace = True)

# long_names = sorted([name for _, name in eu_df["name_long"].items()])
# shorthands = sorted(list(set([name for name in gpg_df["name_long"]])))

merged_df  = eu_df.merge(gpg_df, on="name_long", how="left")
merged_gdf = gpd.GeoDataFrame(merged_df)

filter_2020 = merged_gdf["year"] == 2020
merged_gdf = merged_gdf.loc[filter_2020]
merged_gdf["gap"] = merged_gdf["gap"].fillna(-9999)

mean_gap = merged_gdf["gap"].mean()

for _, i in merged_gdf["gap"].items():
    print(mean_gap-i)

map = KeplerGl()
map.add_data(data=merged_gdf, name="GDF")
map.save_to_html(file_name = "Day03_Polygons.html")
