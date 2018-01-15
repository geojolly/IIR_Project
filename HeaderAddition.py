from pandas import read_csv

df=read_csv("us_active_merged.csv")

df.columns=["text","created","screenName","longitude","latitude","decHour","Hour","minute","zone"]

df.to_csv("mergedheader.csv")