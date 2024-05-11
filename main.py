from pprint import pprint
from API_Pulls import NHLAPIAccessor, NHLAPI_base

src = NHLAPIAccessor
schedule = src.getSchedule("1985-12-25")

print(schedule)



