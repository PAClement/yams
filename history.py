import os

import display
import bdd

class History:

    display = display.Display()
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

    def gameHistoryMenu(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        self.display.titleDisplay("HISTORIC")

        list = self.bdd.getGames()
        tab_Game = []

        print("--------------------------\nGame History\n--------------------------")

        for i in range(len(list)):
            print("Game : ", list[i][0] , " Score = ", list[i][1])
            tab_Game.append(list[i][0])

        print("--------------------------")

        tab_Game.append("Back to menu")

        res = self.display.input_inquirer_list("choices", "Choose your game", tab_Game)
        if(res['choices'] != "Back to menu"):
          self.oneGameHistory(res['choices'])

    def oneGameHistory(self,game_id):
        os.system('cls' if os.name == 'nt' else 'clear')

        self.display.titleDisplay("GAME " + str(game_id))

        listGame = self.bdd.getOnGameWithParty(game_id)

        j = 4
        for i in range(2):
          for key,value in self.score_tab[i].items():
            
            self.score_tab[i][key] = listGame[j]

            j += 1
        
        self.display.display_scoreboard("TOTAL", listGame[1], self.score_tab)

        res = self.display.input_inquirer_list("return", "", ["Return"])

        if(res['return']):
          self.gameHistoryMenu()