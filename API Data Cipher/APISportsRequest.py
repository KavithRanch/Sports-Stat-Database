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
bookmakers_list = ['fanduel', 'draftkings', 'betmgm', 'betrivers', 'barstool']

sport = sports_list[1]
bookmaker = bookmakers_list[0] + "," + bookmakers_list[1] + "," + bookmakers_list[3] + "," + bookmakers_list[4]
odd_format = odd_formatting_list[1]
sports_response = requests.get(f'https://api.the-odds-api.com/v4/sports/{sport}/odds/?bookmakers={bookmaker}&oddsFormat={odd_format}&apiKey={api_key}')
data = sports_response.json()



def getGameInfo(response):
    dates = []
    home_teams = []
    away_teams = []
    home_teams_odds = []
    away_teams_odds = []

    for gameNum in range(len(response)):
        dates.append(response[gameNum]['commence_time'])
        home_teams.append(response[gameNum]['home_team'])
        away_teams.append(response[gameNum]['away_team'])

        home_odds = {}
        away_odds = {}

        for book_maker in response[gameNum]['bookmakers']:
            if book_maker['markets'][0]['outcomes'][0]['name'] == home_teams[-1]:
                home_odds.update({book_maker['title']: book_maker['markets'][0]['outcomes'][0]['price']})
                away_odds.update({book_maker['title']: book_maker['markets'][0]['outcomes'][1]['price']})
            else:
                home_odds.update({book_maker['title']: book_maker['markets'][0]['outcomes'][1]['price']})
                away_odds.update({book_maker['title']: book_maker['markets'][0]['outcomes'][0]['price']})

        home_teams_odds.append(home_odds)
        away_teams_odds.append(away_odds)

    return dates, home_teams, away_teams, home_teams_odds, away_teams_odds


dates, home_teams, away_teams, ht_odds, at_odds = getGameInfo(data)


print("----------------------\nREQUESTS REMAINING: " + sports_response.headers.get("x-requests-remaining") + "\n----------------------")