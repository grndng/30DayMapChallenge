"""30 Day Map Challenge | Day 04: Green (free public transport, people!)

I was looking for the "greenest" city in Europe and stumbled 
upon the website of the European Commission which, each year,
awards a city with the "European Green Capital Award". Next
years winner is Tallinn, the capital of Estonia. Looking up
Tallinn, I've seen quite some greenery in Mustamäe. Mustamäe
translates to "Black Hill" which, in fact, looked pretty green
from above which is why I decided to show it in todays map! 
"""

import osmnx as ox
import matplotlib.pyplot as plt

# Just in case...
ox.config(timeout=10000)

# We set the place we want to look up OSM data in
# and get the outline to work with later on
place = "Tallinn-Mustamäe"
base = ox.geocode_to_gdf(place)

# Setting up tags for buildings and "green areas"
buildings = {"building": True}
greenery = {"leisure":"park", "landuse":"grass"}

# Let's get the roads which come with nodes and edges
roads = ox.graph_from_place(place)

# Only edges looks cleaner, so we ditch the nodes
_, edges = ox.graph_to_gdfs(roads)

# Let's get us some buildings and "G R E E N"-ery
tallinn_buildings = ox.geometries_from_place(place, buildings)
tallinn_greenery = ox.geometries_from_place(place, greenery)

# aaaaand plot!
fig, ax = plt.subplots(figsize=(18,14))
base.plot(ax=ax, facecolor="lightgray")
edges.plot(ax=ax, linewidth=1, edgecolor="darkgray", alpha=0.3)
tallinn_buildings.plot(ax=ax, facecolor="darkgray", alpha=0.3)
tallinn_greenery.plot(ax=ax, facecolor="green")

ax.set_facecolor("white")
plt.tight_layout()

plt.show()
# plt.savefig("Day04/Day04_Green.png")
