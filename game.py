import dice
import combination
import score


class Game:

    rule = None

    def playGame(self):
        print("Game started !")
        
        d = dice.Dices()
        tab = d.roll(5)
        print(tab)
        # TODO Loop le tableau tab et stocker les valeurs gardées par le joueur


play = Game()
play.playGame()
