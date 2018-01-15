import pandas as pd
from timezonefinder import TimezoneFinder
from tzwhere import tzwhere

#Load the csv and creation of dataframes
data=pd.read_csv("us.csv")
df=pd.DataFrame(data, columns=['Hour','Nickname','Latitude','Longitude','minute','timezone'])

#Create a temporary dataframe for writing the zones on fly
tmp=pd.DataFrame(columns=['zone'])

#print(df.iloc[0:100,0:5]) #test the indexes and the updates fuctions

#Method declatation tzwehre
w = tzwhere.tzwhere()

#Converting the lat long to the Zones
for index, row in df.iterrows():
         lat= row['Latitude']
         lon=row['Longitude']
         val=(w.tzNameAt(lat, lon))
         tmp.set_value(index,'zone',val)

print (tmp)

#Wrtite the frame to file with zones
tmp.to_csv('city_zones.csv', header=False)

#Converting the lat long to the Zones
for index, row in df.iterrows():
        lat= row["latitude"]
        lon=row["longitude"]
        name=row["screenName"]
        try:
                val = w.tzNameAt(lat, lon)
                print (index, name, lat, lon, val)
                tmp.set_value(index,"text",row["text"])
                tmp.set_value(index, "created", row["created"])
                tmp.set_value(index, "screenName", row["screenName"])
                tmp.set_value(index, "longitude", row["longitude"])
                tmp.set_value(index, "latitude", row["latitude"])
                tmp.set_value(index, "decHour", row["decHour"])
                tmp.set_value(index, "Hour", row["Hour"])
                tmp.set_value(index, "minute", row["minute"])
                tmp.set_value(index, "zone", val)
        except KeyError:
                print "KeyError"
