"""30 Day Map Challenge | Day 08: OpenStreetMap (not my first time)

I'm using OSMnx and accessing OpenStreetMap data all the time so
I'll just continue doing that. Today we look at bars and pubs in
St. Pauli which is full of bars and music clubs.
"""

import osmnx as ox
import matplotlib.pyplot as plt

# I'll use "place0" as background place and get the
# roads and buildings as well since I don't want 
# the surroundings of the final map to have too much 
# whitespace
place0 = "Hamburg"
place = "Hamburg-St. Pauli"

bars = ox.geometries_from_place(place, tags={"amenity": "bar"})
pubs = ox.geometries_from_place(place, tags={"amenity": "pub"})

area0 = ox.geocode_to_gdf(place0)
area = ox.geocode_to_gdf(place)
buildings = ox.geometries_from_place(place, tags={"building": True})
roads0 = ox.graph_from_place(place0)
_, edges0 = ox.graph_to_gdfs(roads0)
roads = ox.graph_from_place(place)
_, edges = ox.graph_to_gdfs(roads)

fig, ax = plt.subplots(figsize = (18,14))
area.plot(ax = ax, facecolor = "black")
area0.plot(ax=ax, facecolor = "gray", alpha=0.2)
edges.plot(ax = ax, edgecolor = "#cccccc", linewidth = 1)
edges0.plot(ax = ax, edgecolor = "#cccccc", linewidth = 1, alpha = 0.2)
buildings.plot(ax = ax, facecolor = "grey", alpha = 0.7)
bars.plot(ax = ax, color = "yellow", markersize = 15)
pubs.plot(ax = ax, color = "red", markersize = 15)
plt.tight_layout()

plt.show()