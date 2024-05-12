from pprint import pprint
import pandas as pd
from API_Pulls import NHLAPIAccessor, NHLAPI_base

src = NHLAPIAccessor

try:
    schedule = src.getSchedule("2022-03-15")
except:
    print("No Schedule Avaliable")
    schedule = None

print(schedule)

try:
    stats = pd.concat([src.getBoxScore(ID) for ID in schedule['id']], ignore_index=True)
except:
    print("No Stats Avaliable")
    stats = None

print(stats)

