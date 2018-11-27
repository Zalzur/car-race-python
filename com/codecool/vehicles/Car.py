from com.codecool.vehicles.Vehicle import Vehicle
import random


class Car(Vehicle):

    __LOW_SPEED = 80
    __TOP_SPEED = 110
    __CAR_NAME_LIST = ["Prime", "Marvel", "Pinnacle", "Chase", "Renegade",
                       "Ethereal", "Legend", "Guardian", "Vertex", "Encounter"]

    def __init__(self):
        name = "{0} {1}".format(Car.__CAR_NAME_LIST[random.randint(0, len(Car.__CAR_NAME_LIST)-1)],
                                Car.__CAR_NAME_LIST[random.randint(0, len(Car.__CAR_NAME_LIST)-1)])
        speed = random.randint(Car.__LOW_SPEED, Car.__TOP_SPEED + 1)
        distance_traveled = 0
        super(Car, self).__init__(name, speed, distance_traveled)

    def move_for_an_hour(self):
        """TODO: Finish implementation when broken truck is ready"""
        self.distance_traveled += self.speed

    def __repr__(self):
        return self.name + " - " + str(self.distance_traveled)
