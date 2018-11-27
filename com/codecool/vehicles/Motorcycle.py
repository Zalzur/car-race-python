import random
from com.codecool.vehicles.Vehicle import Vehicle
from com.codecool.weather.Weather import Weather


class Motorcycle(Vehicle):

    __MAX_SPEED_LOSS = 50
    __MIN_SPEED_LOSS = 5
    name_counter = 1

    def __init__(self):
        name = "Motorcycle " + str(Motorcycle.name_counter)
        Motorcycle.name_counter += 1
        speed = 100
        distance_traveled = 0
        super(Motorcycle, self).__init__(name, speed, distance_traveled)
        self.rain_speed = speed - random.randint(Motorcycle.__MIN_SPEED_LOSS, Motorcycle.__MAX_SPEED_LOSS)

    def move_for_an_hour(self):
        """TODO: Finis implementation when Truck is ready"""
        self.distance_traveled += self.speed

    def __repr__(self):
        return self.name + " - " + str(self.distance_traveled)
