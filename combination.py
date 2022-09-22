import re
import numpy as np


class Combination:

    def get_combination(self, player_dice):

        score_model = [
            {
                "1": None, "2": None, "3": None,
                "4": None, "5": None, "6": None
            },

            {
                "brelan": None, "square": None, "full": None,
                "small_suite": None, "big_suite": None, "yams": None, "chance": True
            }
        ]

        full_tab = []  # for full combination

        i = 1
        for key, value in score_model[0].items():

            count = np.count_nonzero(np.array(player_dice) == i)

            if (count != 0):
                full_tab.append(count)

            if (count >= 4):
                score_model[1]['square'] = True
            if (count >= 3):
                score_model[1]['brelan'] = True
            if (count == 5):
                score_model[1]['yams'] = True
            if (count > 0):
                score_model[0][key] = True
            i = i + 1

        # Check if player dice is a full
        if ((len(full_tab) == 2) and ((full_tab[0] == 3 and full_tab[1] == 2) or (full_tab[0] == 2 and full_tab[1]))):
            score_model[1]['full'] = True

        sorted_player_dice = sorted(player_dice)
        list_number = ''.join(str(x) for x in sorted_player_dice)  # Join tab

        if (re.match("1234", list_number) or re.match("2345", list_number) or re.match("3456", list_number)):
            score_model[1]['small_suite'] = True

        if (re.match("23456", list_number) or re.match("12345", list_number)):
            score_model[1]['big_suite'] = True

        return score_model
