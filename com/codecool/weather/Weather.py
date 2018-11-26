import random


class Weather:

    __raining = False

    @staticmethod
    def set_raining():
        chance = random.randint(0, 9)
        if chance < 3:
            Weather.__raining = True
        else:
            Weather.__raining = False

    @staticmethod
    def is_raining():
        return Weather.__raining
