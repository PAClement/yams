import os
import bcolor
import inquirer
import pyfiglet
import game


class Menu:

    colors = bcolor.Bcolors()

    game = game.Game()

    def __init__(self):
        pass

    def start_game(self):

        option = None
        while (option != "Quit"):
            os.system('cls' if os.name == 'nt' else 'clear')

            print(pyfiglet.figlet_format("YAMS"))

            choices = [
                inquirer.List(
                    "choices",
                    message="Make your choice ",
                    choices=["Start new game", "Quit"],
                ),
            ]

            res = inquirer.prompt(choices)
            option = res['choices']

            if (option == "Start new game"):
                self.game.playGame()


play = Menu()
play.start_game()
