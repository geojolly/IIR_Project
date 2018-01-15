from datetime import date, timedelta
import matplotlib.pyplot as plt
import pandas as pd
# these lines are just there to create some data
from random import randint
from datetime import datetime
import datefinder

data=pd.read_csv("realDonaldTrump_tweets.csv")
df=pd.DataFrame(data, columns=["id","created_at","text"])
print(df["created_at"])
dates=df["created_at"]
dates.to_numeric(dates)
for index , row in df:
    matches = datefinder.find_dates(dates)
    for match in matches:
        print match