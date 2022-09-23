import os
from prettytable import PrettyTable

import dice
import combination
import score
import display


class Game:

    dices = dice.Dices()
    combination = combination.Combination()
    score = score.Score()
    display = display.Display()

    tab_dice = []

    def get_dice(self):
        for i in range(3):
            print("Lancer les dés...")

            current_roll = self.dices.roll(5 - len(self.tab_dice))

            if (i < 2):
                if (len(self.tab_dice) != 0):
                    print("Vos dés : ", self.tab_dice)

                print("Nouveau lancé : ", current_roll)
                res = self.display.input_inquirer_list("roll_dice", "keep dice, reroll All ou stop ?", ['keep dice', 'reroll', 'stop'])

                start_stop = res['roll_dice']

                if (start_stop == "keep dice" and len(self.tab_dice) < 5):
                    print("Vos dés : ")
                    print("Quels dés voulez-vous garder ?", current_roll, " | input la valeur des dés : patern 1,2,3")

                    keep_dice = input()
                    for j in keep_dice:
                        if (j != ','):
                            if (len(self.tab_dice) < 5):
                                self.tab_dice.append(int(j))
                elif (start_stop == "reroll"):
                    continue
                else:
                    for j in current_roll:
                        if (len(self.tab_dice) < 5):
                            self.tab_dice.append(int(j))

                    return

        for j in current_roll:
            if (len(self.tab_dice) < 5):
                self.tab_dice.append(int(j))

    def playGame(self):
        self.score.scoreboard_to_zero()

        print("Game started !")

        while True:

            self.display.display_scoreboard("Combination", "Yours points",  self.score.current_scoreboard())

            # Retrieve players dice after 3 round
            self.tab_dice = []
            self.get_dice()

            self.split_if_model_is_empty_or_not(self.score.score_available(self.combination.get_combination(self.tab_dice)))

            os.system('cls' if os.name == 'nt' else 'clear')

            # verify if scoreboard is full
            if (self.score.state_scoreboard()):
                break

        print("GAME ENDED !")

        scoreboard = self.score.get_scoreboard()
        self.display.display_scoreboard("Total", scoreboard[0], scoreboard[1])

        # Input for return to the menu
        self.display.input_inquirer_list("return_menu", "GG !", ["Back to the menu"])

    def split_if_model_is_empty_or_not(self, model_scored):

        if (len(model_scored) != 0):
            print("Vos dés ", self.tab_dice)

            res = self.display.input_inquirer_list("combination", "Quelle combinaison voulez-vous ?", model_scored)

            print(res['combination'])

            # set score on scoreboard
            self.score.set_scored(res['combination'], self.tab_dice)
        else:

            res_set_to_zero = self.display.input_inquirer_list("combination_to_zero", "Quelle combinaison voulez-vous mettre à zéro ? ", self.score.get_unscore_tab())

            self.score.set_score_to_zero(res_set_to_zero['combination_to_zero'])
