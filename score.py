
from distutils.log import debug
import numpy as np
import bdd

class Score:

    bdd = bdd.Bdd()

    score_tab = [
        {
            "1": None, "2": None, "3": None,
            "4": None, "5": None, "6": None
        },
        {
            "brelan": None, "square": None, "full": None,
            "small_suite": None, "big_suite": None, "yams": None, "chance": None
        }
    ]

    bonus = None  # if all point before is upper than 62, bonus = +35

    def reload_scoreboard(self):
        self.score_tab = [
            {
                "1": None, "2": None, "3": None,
                "4": None, "5": None, "6": None
            },
            {
                "brelan": None, "square": None, "full": None,
                "small_suite": None, "big_suite": None, "yams": None, "chance": None
            }
        ]
        
        last_party = self.bdd.getLastParty()

        if( last_party != None):
            
            j = 0
            for i in range(2):
                for key, value in self.score_tab[i].items():
                    self.score_tab[i][key] = last_party[j]
                    j += 1

            return False
        
        return True



    def score_available(self, model):

        available_place = []
        for i in range(2):
            for key, value in model[i].items():

                if (self.score_tab[i][key] != None):

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
                self.bdd.setScore("one", count * 1 )
            case "2":
                count = np.count_nonzero(np.array(player_dice) == 2)
                self.score_tab[0]["2"] = count * 2
                self.bdd.setScore("two", count * 2 )
            case "3":
                count = np.count_nonzero(np.array(player_dice) == 3)
                self.score_tab[0]["3"] = count * 3
                self.bdd.setScore("three", count * 3 )
            case "4":
                count = np.count_nonzero(np.array(player_dice) == 4)
                self.score_tab[0]["4"] = count * 4
                self.bdd.setScore("four", count * 4 )
            case "5":
                count = np.count_nonzero(np.array(player_dice) == 5)
                self.score_tab[0]["5"] = count * 5
                self.bdd.setScore("five", count * 5 )
            case "6":
                count = np.count_nonzero(np.array(player_dice) == 6)
                self.score_tab[0]["6"] = count * 6
                self.bdd.setScore("six", count * 6 )
            case "brelan":
                brelan_tab = np.array(player_dice)

                for i in range(6):
                    count = np.count_nonzero(brelan_tab == i+1)
                    if (count >= 3):
                        self.score_tab[1]["brelan"] = 3 * (i+1)
                        self.bdd.setScore("brelan",  3 * (i+1) )
            case "square":
                square_tab = np.array(player_dice)

                for i in range(6):
                    count = np.count_nonzero(square_tab == i+1)
                    if (count >= 3):
                        self.score_tab[1]["square"] = 4 * (i+1)
                        self.bdd.setScore("square",  4 * (i+1) )
            case "full":
                self.score_tab[1]["full"] = 25
                self.bdd.setScore("full",  25 )
            case "small_suite":
                self.score_tab[1]["small_suite"] = 30
                self.bdd.setScore("small_suite",  30 )
            case "big_suite":
                self.score_tab[1]["big_suite"] = 40
                self.bdd.setScore("big_suite",  40 )
            case "yams":
                self.score_tab[1]["yams"] = 50
                self.bdd.setScore("yams",  50 )
            case "chance":
                dice_sum = np.sum(player_dice)
                self.score_tab[1]["chance"] = dice_sum
                self.bdd.setScore("chance",  int(dice_sum) )

        return self.score_tab

    def state_scoreboard(self):

        for i in range(2):
            for key, value in self.score_tab[i].items():

                if (self.score_tab[i][key] == None):
                    return False

        return True

    def get_unscore_tab(self):

        delete_tab = []

        for i in range(2):
            for key, value in self.score_tab[i].items():

                if (self.score_tab[i][key] == None):
                    delete_tab.append(key)

        return delete_tab

    def set_score_to_zero(self, value_key):

        for i in range(2):
            if value_key in self.score_tab[i].keys():
                self.score_tab[i][value_key] = 0

        return self.score_tab

    def get_scoreboard(self):

        final_scoreboard = []
        score = 0

        for i in range(2):
            for key, value in self.score_tab[i].items():

                score = score + value

        final_scoreboard.append(score)
        final_scoreboard.append(self.score_tab)
        return final_scoreboard

    def current_scoreboard(self):

        return self.score_tab
