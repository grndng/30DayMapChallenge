"""30 Day Map Challenge | Day 05: Ukraine (254 days...)

For Day 05: Ukraine I was really undecided what to do without
doing something obvious and might have ended up doing something
obvious: Snake Island. Since I'm trying to solve all 30 days 
with Python, I thought it might be appropriate to do Snake Island
or Zmiinyi Island.
"""

import osmnx as ox
import matplotlib.pyplot as plt

# We set the place we want to look up OSM data in
# and get the outline to work with later on
place = "Zmiinyi Island"
base = ox.geocode_to_gdf(place)

# Setting up tags (should simplify here...)
buildings = {"building": True, "landuse":"harbour"}
greenery = {"leisure":True, "landuse":"grass"}
man_made_structures = {"man_made":"monitoring_station", "landuse":"residential", "man_made":"breakwater"}
pier = {"man_made":"pier"}
beach = {"natural":"beach"}
historic = {"historic":True}
tourism = {"tourism":True}
lattice = {"man_made":"mast"}
helipad = {"aeroway":"helipad"}
cliff = {"natural":"cliff"}

# Let's get the roads which come with nodes and edges
# Only edges looks cleaner, so we ditch the nodes
_, edges = ox.graph_to_gdfs(ox.graph_from_place(place))

# Writing a function to get the geometries...
def get_geoms(tags, place = place):
    return ox.geometries_from_place(place, tags)

# aaaaand plot (and also simplify)!
fig, ax = plt.subplots(figsize=(18,14))
base.plot(ax=ax, facecolor="#b1c693")
edges.plot(ax=ax, linewidth=1, edgecolor="darkgray", alpha=0.5)
get_geoms(man_made_structures).plot(ax=ax, facecolor="lightgray", alpha=0.5)
get_geoms(buildings).plot(ax=ax, facecolor="darkgray", alpha=0.6)
get_geoms(greenery).plot(ax=ax, facecolor="#6d9e29", alpha=1)
get_geoms(historic).plot(ax=ax, facecolor="#6f3970") # Greek Temple to Achilles
get_geoms(tourism).plot(ax=ax, facecolor="#6f3970", alpha=0.5)
get_geoms(beach).plot(ax=ax, facecolor="beige")
get_geoms(lattice).plot(ax=ax, facecolor="silver")
get_geoms(helipad).plot(ax=ax, facecolor="white", alpha=0.3)
get_geoms(cliff).plot(ax=ax, edgecolor="brown", alpha=0.4)
get_geoms(pier).plot(ax=ax, facecolor="gray", alpha=0.4)

ax.set_facecolor("white")
plt.tight_layout()

plt.show()
#plt.savefig("Day05/Day05_Ukraine.png")
