import numpy as np


class Score:

    score_tab = [
        {
            "1": "6", "2": False, "3": False,
            "4": False, "5": False, "6": False
        },
        {
            "brelan": "18", "square": False, "full": False,
            "small_suite": False, "big_suite": "40", "yams": False, "chance": False
        }
    ]

    # brelan = None
    # square = None
    # full = None  # +25
    # small_suite = None  # +30
    # big_suite = None  # +40
    # yams = None  # +50

    bonus = None  # if all point before is upper than 62, bonus = +35

    sum_point = 0

    def score_verification(self, model):

        available_place = []
        for i in range(2):
            for key, value in model[i].items():

                if (self.score_tab[i][key] != False):

                    # this score is not empty
                    model[i][key] = self.score_tab[i][key]
                elif (model[i][key] == True):

                    available_place.append(key)

        return available_place

    def set_scored(self, combi, player_dice):

        match combi:

            case "1":
                count = np.count_nonzero(np.array(player_dice) == 1)
                self.score_tab[0]["1"] = count * 1
            case "2":
                count = np.count_nonzero(np.array(player_dice) == 2)
                self.score_tab[0]["2"] = count * 2
            case "3":
                count = np.count_nonzero(np.array(player_dice) == 3)
                self.score_tab[0]["3"] = count * 3
            case "4":
                count = np.count_nonzero(np.array(player_dice) == 4)
                self.score_tab[0]["4"] = count * 4
            case "5":
                count = np.count_nonzero(np.array(player_dice) == 5)
                self.score_tab[0]["5"] = count * 5
            case "6":
                count = np.count_nonzero(np.array(player_dice) == 6)
                self.score_tab[0]["6"] = count * 6
            case "brelan":
                pass
            case "square":
                pass
            case "full":
                self.score_tab[1]["full"] = 25
            case "small_suite":
                self.score_tab[1]["small_suite"] = 30
            case "big_suite":
                self.score_tab[1]["big_suite"] = 40
            case "yams":
                self.score_tab[1]["yams"] = 50
            case "chance":
                dice_sum = np.sum(player_dice)
                self.score_tab[1]["chance"] = dice_sum

        return self.score_tab
