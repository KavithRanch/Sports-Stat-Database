'''
Online Sports Odds Webscraper
Developed by Kavith Ranchagoda
Using 'odd-api' API

Endpoint formatting: https://api.the-odds-api.com/v4/sports/[SPORTS]/odds/?bookmakers=[BOOKMAKERS]&oddsFormat=[ODDSFORMAT]&apiKey=[APIKEY]
'''
import requests

api_key = 'd53a635c6f06ac165ea39e78a995a353'

sports_list = ['americanfootball_nfl', 'americanfootball_ncaaf', 'basketball_nba', 'baseball_mlb', 'icehockey_nhl']
odd_formatting_list = ['american', 'decimal']
bookmakers_list = ['fanduel', 'draftkings', 'betmgm', 'betrivers']

sport = sports_list[0]
bookmaker = bookmakers_list[0] + "," + bookmakers_list[1]
sports_response = requests.get(f'https://api.the-odds-api.com/v4/sports/{sport}/odds/?bookmakers={bookmaker}&oddsFormat=american&apiKey={api_key}')
data = sports_response.json()



def getGameInfo(response):
    dates = []
    home_teams = []
    away_teams = []
    home_teams_oddsFD = []
    away_teams_oddsFD = []
    home_teams_oddsDK = []
    away_teams_oddsDK = []

    for gameNum in range(len(response)):
        dates.append(response[gameNum]['commence_time'])
        home_teams.append(response[gameNum]['home_team'])
        away_teams.append(response[gameNum]['away_team'])

        if response[gameNum]['bookmakers'][0]['markets'][0]['outcomes'][0]['name'] == home_teams[-1]:
            home_teams_oddsFD.append(response[gameNum]['bookmakers'][0]['markets'][0]['outcomes'][0]['price'])
            away_teams_oddsFD.append(response[gameNum]['bookmakers'][0]['markets'][0]['outcomes'][1]['price'])
            home_teams_oddsDK.append(response[gameNum]['bookmakers'][1]['markets'][0]['outcomes'][0]['price'])
            away_teams_oddsDK.append(response[gameNum]['bookmakers'][1]['markets'][0]['outcomes'][1]['price'])
        else:
            home_teams_oddsFD.append(response[gameNum]['bookmakers'][0]['markets'][0]['outcomes'][1]['price'])
            away_teams_oddsFD.append(response[gameNum]['bookmakers'][0]['markets'][0]['outcomes'][0]['price'])
            home_teams_oddsDK.append(response[gameNum]['bookmakers'][1]['markets'][0]['outcomes'][1]['price'])
            away_teams_oddsDK.append(response[gameNum]['bookmakers'][1]['markets'][0]['outcomes'][0]['price'])

    return dates, home_teams, away_teams, home_teams_oddsFD, home_teams_oddsDK, away_teams_oddsFD, away_teams_oddsDK


dates, home_teams, away_teams, ht_odds_FD, ht_odds_DK, at_odds_FD, at_odds_DK = getGameInfo(data)


x = 4
print("On " + str(dates[x]) + ", the " + str(away_teams[x]) + "(" + str(at_odds_FD[x]) + ") are playing at the " + str(home_teams[x]) + "(" + str(ht_odds_FD[x]) + ")")

print("----------------------\nREQUESTS REMAINING: " + sports_response.headers.get("x-requests-remaining") + "\n----------------------")