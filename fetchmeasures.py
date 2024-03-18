import requests
import pandas as pd

#import json
raindata = requests.get("https://environment.data.gov.uk/flood-monitoring/id/measures?label=rainfall-tipping_bucket_raingauge-t-15_min-mm")
stationdata = requests.get("https://environment.data.gov.uk/flood-monitoring/id/stations?qualifier=Tipping%20Bucket%20Raingauge")


#create dataframe
measures = pd.json_normalize(raindata.json()["items"])
stationlist = pd.json_normalize(stationdata.json()["items"])

#reduce columns
measures = measures[["stationReference","latestReading.date","latestReading.value"]]
stationlist = stationlist[["@id", "stationReference", "easting", "northing", "lat", "long"]]

#create CSVs (optional)
#measures.to_csv("measures.csv", index=False)
#stationlist.to_csv("stationlist.csv", index=False)


finaldata = pd.merge(stationlist, measures, how="left", on="stationReference")

finaldata.to_csv("finaldata.csv", index=False)

print("done")
