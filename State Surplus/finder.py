import pandas as pd

parcels = pd.read_csv("final_data.csv")

count = 0

for parcel in parcels.iterrows():
    data = parcel[1]
    if type(data["District"]) != float and data["District"] == "2nd Middlesex District" and data["luc_adj_2"] in [973, 974]:
        count += 1
        print(data["site_addr"])

print(count)