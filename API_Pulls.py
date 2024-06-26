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
        
        # cols = ['date', 'id', 'season', 'gameType',
        #         'awayTeam.id', 'awayTeam.abbrev', 'awayTeam.score',
        #         'homeTeam.id', 'homeTeam.abbrev', 'homeTeam.score',
        #         'gameOutcome.lastPeriodType']

        return df


    def getBoxScore(gameID):
        data = requests.get(NHLAPI_base+f"gamecenter/{gameID}/boxscore").json()

        try:
            dataPD = pd.json_normalize(data['playerByGameStats'])
            df = []
            for col in dataPD.columns:
                for p in range(0, len(dataPD[col][0])):
                    rw = dataPD[col][0][p]
                    rw['team'] = col.split('.')[0]
                    rw['positionGrp'] = col.split('.')[1]
                    df.append(rw)
            
            df = pd.json_normalize(df)
        except:
            df = None
        return df

class NHLadvanced:

    def MPplayers(season, team):
        
        storage_options = {'User-Agent': 'Mozilla/5.0'}
        data = pd.read_csv(f"https://moneypuck.com/moneypuck/playerData/teamPlayerGameByGame/{season}/regular/skaters/{team}.csv", storage_options=storage_options)

        return data