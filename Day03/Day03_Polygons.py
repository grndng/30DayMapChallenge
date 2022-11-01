"""30 Day Map Challenge | Day 03: Polygons (Gender Pay Gap)

I've read an article about the gender pay gap and how
it is still a problem in most places. I've first taken
a look at data in Germany but thought that maybe stepping
back and taking a look at Europe would make sense, too.
"""

import geopandas as gpd
import pandas as pd

gpg_df = gpd.read_file("./Day03/data/gender_pay_gap_eurostat.csv")
eu_df = gpd.read_file("./Day03/data/europe.json")

print(gpg_df)