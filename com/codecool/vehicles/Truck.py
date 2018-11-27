import random
from com.codecool.vehicles.Vehicle import Vehicle


class Truck(Vehicle):

    __BREAK_DOWN_TURNS = 2

    def __init__(self):
        name = str(random.randint(0, 1000))
        normal_speed = 100
        distance_traveled = 0
        super().__init__(name, normal_speed, distance_traveled)
        self.break_down_turns_left = 0

    @staticmethod
    def is_broke_down():
        chance = random.randint(0, 99)
        if chance < 5:
            return True
        else:
            return False

    def move_for_an_hour(self, race):
        if self.break_down_turns_left > 0:
            self.break_down_turns_left -= 1
        else:
            if race.is_there_a_broken_truck():
                self.distance_traveled += Vehicle._SPEED_LIMIT_WHEN_BREAKDOWN
                if Truck.is_broke_down():
                    self.break_down_turns_left = Truck.__BREAK_DOWN_TURNS
            else:
                self.distance_traveled += self.normal_speed
                if Truck.is_broke_down():
                    self.break_down_turns_left = Truck.__BREAK_DOWN_TURNS

    def __repr__(self):
        return self.name + " - " + str(self.distance_traveled)
