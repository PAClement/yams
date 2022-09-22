import os
import dice
import combination
import score
import inquirer
from prettytable import PrettyTable


class Game:

    dices = dice.Dices()
    combination = combination.Combination()
    score = score.Score()

    tab_dice = []

    def get_dice(self):
        for i in range(3):
            print("Lancer les dés...")

            current_roll = self.dices.roll(5 - len(self.tab_dice))

            if (i < 2):
                if (len(self.tab_dice) != 0):
                    print("Vos dés : ", self.tab_dice)

                print("Nouveau lancé : ", current_roll)
                roll_dice = [
                    inquirer.List(
                        "roll_dice",
                        message="keep dice, reroll All ou stop ? ",
                        choices=['keep dice', 'reroll', 'stop'],
                    ),
                ]

                res = inquirer.prompt(roll_dice)
                start_stop = res['roll_dice']

                if (start_stop == "keep dice" and len(self.tab_dice) < 5):
                    print("Vos dés : ")
                    print(
                        "Quels dés voulez-vous garder ?", current_roll, " | input la valeur des dés : patern 1,2,3")
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
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Game started !")

        while True:
            # Retrieve players dice after 3 round
            self.tab_dice = []
            self.get_dice()

            # test Combination possible
            model_combination = self.combination.get_combination(self.tab_dice)

            # Verification which score is available
            model_scored = self.score.score_verification(model_combination)

            if (len(model_scored) != 0):
                print("Vos dés ", self.tab_dice)
                combination_question = [
                    inquirer.List(
                        "combination",
                        message="Quelle combinaison voulez-vous ? ",
                        choices=model_scored,
                    ),
                ]

                res = inquirer.prompt(combination_question)
                print(res['combination'])

                # set score on scoreboard
                self.score.set_scored(
                    res['combination'], self.tab_dice)
            else:

                unscore_tab = self.score.get_unscore_tab()

                combination_to_zero_question = [
                    inquirer.List(
                        "combination_to_zero",
                        message="Quelle combinaison voulez-vous mettre à zéro ? ",
                        choices=unscore_tab,
                    ),
                ]

                res_set_to_zero = inquirer.prompt(combination_to_zero_question)

                self.score.set_score_to_zero(
                    res_set_to_zero['combination_to_zero'])

            os.system('cls' if os.name == 'nt' else 'clear')

            # verify if scoreboard is full
            if (self.score.state_scoreboard()):
                break

        print("GAME ENDED !")

        scoreboard = self.score.get_scoreboard()

        cli_tab_score = PrettyTable(['Total', scoreboard[0]])

        for i in range(2):
            for key, value in scoreboard[1][i].items():
                cli_tab_score.add_row([key, value])

        print(cli_tab_score)

        return_menu = [
            inquirer.List(
                "return_menu",
                choices=["Back to the menu"],
            ),
        ]

        res = inquirer.prompt(return_menu)
