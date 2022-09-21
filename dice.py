import random


class Dice:

    nb_face = 6

    __value = None

    def roll(self):
        self.__value = random.randint(1, self.nb_face)

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value


class Dices:

    dices = []
    current_Dice = None

    def __init__(self):
        self.current_Dice = Dice()

    def roll(self, nb_dice):
        self.dices = []
        for i in range(0, nb_dice):
            self.current_Dice.roll()
            self.dices.append(self.current_Dice.get_value())

        return self.dices
