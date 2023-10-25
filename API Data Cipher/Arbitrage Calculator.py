'''
home_teams, away_teams = List of Strings
ht_odds, at_odds = List of Dictionaries (key: 'Odds Site', value: int decimal odd)
'''
from APISportsRequest import home_teams, away_teams, ht_odds, at_odds
import numpy as np

def arbitrage_calculator(prob_matrix):
    if prob_matrix.size != 0:
        result = []
        for rows in prob_matrix:
            max_index = np.argmax(rows)
            imp_prob = 1/max(rows) * 100
            result.append([max_index, round(imp_prob, 2)])

        if result[0][1] + result[1][1] < 100:
            return result
        else:
            print("No Arbitrage Opportunity Available")
    else:
        print("Odds Unavailable")






for game_num in range(len(home_teams)):
    imp_probability = np.zeros((len(ht_odds[game_num]), 2))
    count = 0
    for bookie in ht_odds[game_num]:
        imp_probability[count] = [ht_odds[game_num][bookie], at_odds[game_num][bookie]]
        count += 1

    imp_probability = imp_probability.transpose()
    print("------------\n" + home_teams[game_num] + " VS. " + away_teams[game_num])
    print(imp_probability)
    arb_result = arbitrage_calculator(imp_probability)

ht_odds
odd = 0
imp_probability = 1/200 * 100


