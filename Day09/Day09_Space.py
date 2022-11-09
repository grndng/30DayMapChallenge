"""30DayMapChallenge | Day 09: Space

I had literally no idea what to do for today since I 
don't know any way to plot things in a coordinate system
that's not on our planet. Which is why I decided not to
look at space directly but to people who went to space. 
To be more precise I took a look at the countries of origin
and gender of people who are part of the crew of the 
International Space Station and have visualised it.
"""

import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl
import osmnx as ox

df = pd.read_csv("Day09/data/InternationalAstronautDatabase.csv", index_col=0)
df_general = df.groupby("Country").count()
df_more_than_1 = df_general[df_general["TotalFlights"] > 1]
df_female = df.loc[(df["Gender"]=="Woman")].groupby(["Country"]).count()
fa_more_than_1 = df_female[df_female["Gender"] > 1]

female_country_list = ["Canada","Nippon","Russia","USA"]
male_country_list = ["Belgium", "Bulgaria", "Canada", "China", "France", "Germany", "Hungary", "Italy", "Nippon", "Kasachstan", "Netherlands", "Russia", "United Kingdom", "United States"]

# Loop schreiben um die Länder-Shapes zu geiern
def get_country_shapes(list):
    l = []
    for country in list:
        l.append(ox.geocode_to_gdf(country))
    return l

def generate_kepler_map(countryshapes_male, countryshapes_female):
    map = KeplerGl()
    countries = countryshapes_male[0] # too lazy to create an empty gdf
    for country in countryshapes_male[1:]:
        gdf = gpd.GeoDataFrame(pd.concat([countries, country]))
        countries = gdf
    map.add_data(data=gdf, name="Countries (Male)")

    countries = countryshapes_female[0] # too lazy to create an empty gdf
    for country in countryshapes_female[1:]:
        gdf = gpd.GeoDataFrame(pd.concat([countries, country]))
        countries = gdf
    map.add_data(data=gdf, name="Countries (Female)")

    map.save_to_html(file_name = "Day09/Day09_Space.html")

generate_kepler_map(get_country_shapes(male_country_list), get_country_shapes(female_country_list))