import os

import game
import display
import history
import bdd

class Menu:

    game = game.Game()
    display = display.Display()
    history = history.History()
    bdd = bdd.Bdd()

    def __init__(self):
        self.start_game()

    def start_game(self):

        option = None
        while (option != "Quit"):
            os.system('cls' if os.name == 'nt' else 'clear')

            self.bdd.createTable()
            
            self.display.titleDisplay("YAMS")

            res = self.display.input_inquirer_list("choices", "Make your choice ", ["Start new game", "Game History", "Quit"])

            match res['choices']:
                case "Start new game":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.game.playGame()
                case "Game History":
                    self.history.gameHistoryMenu()
                case "Quit":
                    option = "Quit"

                


play = Menu()
