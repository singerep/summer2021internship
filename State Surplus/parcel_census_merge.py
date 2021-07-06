import pandas as pd

parcels = pd.read_csv("parcel-geoData.csv")

parcels["Gfips"] = "G" + parcels["fips"].astype(str)
parcels["geoid"] = "14000US" + parcels["fips"].astype(str)

print(parcels)