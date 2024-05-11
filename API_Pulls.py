import requests
import pandas as pd

NHLAPI_base = "https://api-web.nhle.com/v1/"


class NHLAPIAccessor:

    def getSchedule(date):
        data = requests.get(NHLAPI_base+f"schedule/{date}").json()
        dataPD = pd.json_normalize(data['gameWeek'])

        df = []

        for dt in range(0, len(dataPD['date'])):
            for gm in range(0, len(dataPD['games'][dt])):
                if dataPD['games'][dt][gm] != []:
                    rw = dataPD['games'][dt][gm]
                    rw['date'] = dataPD['date'][dt]
                    df.append(rw)
                else:
                    continue

        df = pd.json_normalize(df)
        

        cols = ['date', 'id', 'season', 'gameType',
                'awayTeam.id', 'awayTeam.abbrev', 'awayTeam.score',
                'homeTeam.id', 'homeTeam.abbrev', 'homeTeam.score',
                'gameOutcome.lastPeriodType']

        return df[cols]

