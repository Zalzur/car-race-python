import abc


class Vehicle(abc.ABC):

    def __init__(self, name, speed, distance_traveled):
        self.name = name
        self.speed = speed
        self.distance_traveled = distance_traveled

    @abc.abstractmethod
    def move_for_an_hour(self):
        """Moves the vehicle for an hour"""

    @abc.abstractmethod
    def __repr__(self):
        """Prints the information"""
