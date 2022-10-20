"""30 Day Map Challenge | Day 01: Points or "What overseas territories do to your centroid!"

I've tried to find something that's interesting to me and
to start off will provide a quick result so I stay motivated
and don't have to fiddle around too much. This is why I took
France and its centroid as an example. When considering the
overseas areas, the centroid isn't even in Metropolitan France
(according to https://en.wikipedia.org/wiki/Metropolitan_France
the part of France that is geographically in Europe). The same 
applies to Hamburg which has an exclave called "Neuwerk" close
to the North Sea.
"""

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from keplergl import KeplerGl

df = gpd.read_file("data/ne_10m_admin_0_countries.shp")

france_complete = df[df["NAME"] == "France"]
print(type(france_complete))
# francentroid = Point(france_complete["geometry"].centroid.x, france_complete["geometry"].centroid.y)

# Okay, so I specifically checked if all overseas territories of
# France are included because the centroid didn't look right and I
# could not find French Polynesia. While doing so I've noticed that
# there seems to be "French Southern Antarctic Lands"... Need to
# add those too, right?

france_complete = df[df["NAME"].str.startswith("Fr")]

# francentroid = Point(france_complete["geometry"].centroid.x, france_complete["geometry"].centroid.y)


# # At this point: kill me for doing it with keplergl
# df = pd.DataFrame(
#     {'Country': ['France'],
#      'Latitude': [francentroid.y],
#      'Longitude': [francentroid.x]})

# map = KeplerGl()
# map.add_data(data=df, name='Country')
# map.add_data(data = france_complete, name = "France")
# map.save_to_html(file_name = "test.html")

