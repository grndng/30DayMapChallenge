# Zip Scribble?
#https://eagereyes.org/zipscribble-maps/united-states

import pandas as pd

plzdf = pd.read_csv("Day02/data/PLZ.csv", names=["postcode", "cityname", "lon", "lat"], header=None, delimiter=";") # https://launix.de/launix/launix-gibt-plz-datenbank-frei/
