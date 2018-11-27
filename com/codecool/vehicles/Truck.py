import random
from com.codecool.vehicles.Vehicle import Vehicle


class Truck(Vehicle):

    __BREAK_DOWN_TURNS = 2

    def __init__(self):
        name = str(random.randint(0, 1000))
        speed = 100
        distance_traveled = 0
        super().__init__(name, speed, distance_traveled)
        self.break_down_turns_left = 0

    def move_for_an_hour(self):
        """TODO: Finis implementation when race simulation is ready"""
        self.distance_traveled += self.speed

    def __repr__(self):
        return self.name + " - " + str(self.distance_traveled)
