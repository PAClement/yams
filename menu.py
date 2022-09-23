import os
import bcolor
import pyfiglet

import game
import display

class Menu:

    colors = bcolor.Bcolors()
    game = game.Game()
    display = display.Display()

    def __init__(self):
        self.start_game()

    def start_game(self):

        option = None
        while (option != "Quit"):
            os.system('cls' if os.name == 'nt' else 'clear')

            print(pyfiglet.figlet_format("YAMS"))

            res = self.display.input_inquirer_list("choices", "Make your choice ", ["Start new game", "Quit"])
            
            option = res['choices']

            if (option == "Start new game"):
                os.system('cls' if os.name == 'nt' else 'clear')
                self.game.playGame()


play = Menu()
