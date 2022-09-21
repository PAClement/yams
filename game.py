import dice
import combination
import score


class Game:

    dices = dice.Dices()
    combination = combination.Combination()
    score = score.Score()

    tab_dice = []
    rule = None
    point = None

    def get_dice(self):
        for i in range(3):
            print("Lancer les dés...")

            current_roll = self.dices.roll(5 - len(self.tab_dice))
            if (len(self.tab_dice) != 0):
                print("Vos dés : ", self.tab_dice)

            print("Nouveau lancé : ", current_roll)

            print("Continuer ou areter ? | 1 : continuer , 0 : areter")
            start_stop = int(input())

            if (start_stop == 1 and len(self.tab_dice) < 5):
                print("Vos dés : ", current_roll)
                print(
                    "Quels dés voulez-vous garder ? | input la valeur des dés : patern 1,2,3")
                keep_dice = input()
                for i in keep_dice:
                    if (i != ','):
                        self.tab_dice.append(int(i))
            else:
                if (start_stop == 0):
                    for i in current_roll:
                        self.tab_dice.append(int(i))
                return

    def playGame(self):
        print("Game started !")

        # Retrieve players dice after 3 round
        # self.get_dice()
        self.tab_dice = [6, 1, 2, 4, 3]
        # Combination possible test
        self.combination.get_combination(self.tab_dice)


play = Game()
play.playGame()
