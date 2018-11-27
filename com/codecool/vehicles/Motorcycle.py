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
        normal_speed = 100
        distance_traveled = 0
        super(Motorcycle, self).__init__(name, normal_speed, distance_traveled)
        self.rain_speed = normal_speed - random.randint(Motorcycle.__MIN_SPEED_LOSS, Motorcycle.__MAX_SPEED_LOSS)

    def move_for_an_hour(self, race):
        if Weather.is_raining():
            if race.is_there_a_broken_truck() and self.rain_speed > Vehicle._SPEED_LIMIT_WHEN_BREAKDOWN:
                self.distance_traveled += Vehicle._SPEED_LIMIT_WHEN_BREAKDOWN
            else:
                self.distance_traveled += self.rain_speed
        else:
            if race.is_there_a_broken_truck():
                self.distance_traveled += Vehicle._SPEED_LIMIT_WHEN_BREAKDOWN
            else:
                self.distance_traveled += self.normal_speed

    def __repr__(self):
        return self.name + " - " + str(self.distance_traveled)
