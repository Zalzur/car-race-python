import random


class Weather:

    raining = False

    @staticmethod
    def set_raining():
        chance = random.randint(0, 9)
        print(chance)
        if chance < 3:
            Weather.raining = True
        else:
            Weather.raining = False

    @staticmethod
    def is_raining():
        return Weather.raining
