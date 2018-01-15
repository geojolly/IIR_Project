import pandas as pd
from timezonefinder import TimezoneFinder
from tzwhere import tzwhere

#Load the csv and creation of dataframes
data=pd.read_csv("unique_coordinates_geo.csv")
df=pd.DataFrame(data, columns=["longitude","latitude"])


#Create a temporary dataframe for writing the zones on fly
tmp=pd.DataFrame(columns=["longitude","latitude","zone"])

#Method declatation tzwehre
w = tzwhere.tzwhere()

#Converting the lat long to the Zones
for index, row in df.iterrows():
        lat= row["latitude"]
        lon=row["longitude"]
        try:
                val = w.tzNameAt(lat, lon)
                print (index, lat, lon, val)
                tmp.set_value(index, "longitude", row["longitude"])
                tmp.set_value(index, "latitude", row["latitude"])
                tmp.set_value(index, "zone", val)
        except KeyError:
                print "KeyError"

#Wrtite the frame to file with zones
tmp.to_csv('zones_geo.csv', header=True)