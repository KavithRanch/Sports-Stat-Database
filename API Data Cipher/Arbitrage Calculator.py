'''
Calculate whether Arbitrage opportunity is available
Returns to user which market to bet which odd for a specific prop to guarantee win

Format of variables dependent on:
home_teams, away_teams, bookmakers_list = List of Strings
ht_odds, at_odds = List of Dictionaries (key: 'Odds Site', value: int decimal odd)
'''
from APISportsRequest import home_teams, away_teams, ht_odds, at_odds, bookmakers_list
import numpy as np


def arbitrage_calculator(prob_matrix):
    if prob_matrix.size != 0:
        result = []
        for rows in prob_matrix:
            max_index = np.argmax(rows)
            imp_prob = 1/max(rows) * 100
            result.append([max_index, round(imp_prob, 2)])

        arbSum = 0
        for elements in range(len(result)): # Some selections may have > 2 options
            arbSum += result[elements][1]

        print(arbSum)
        if arbSum < 100:
            return result

        else:
            print("No Arbitrage Opportunity Available")
            return []
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
    result = arbitrage_calculator(imp_probability)
    print(result)

    if result:
        total_stake = 100
        total_imp_prob = result[0][1] + result[1][1]
        bet_on_home = total_stake * result[0][1] / total_imp_prob
        bet_on_away = total_stake * result[1][1] / total_imp_prob
        profit = total_stake / total_imp_prob - total_stake

        print("With $100 stake:\nBet $" + str(bet_on_home) + " on the " + home_teams[game_num] + " ML on " + bookmakers_list[result[0][0]] + "\nBet $" + str(bet_on_away) + " on the " + away_teams[game_num] + " ML on " + bookmakers_list[result[1][0]] + "\nThis wins $" + str(profit) + " in profit")



