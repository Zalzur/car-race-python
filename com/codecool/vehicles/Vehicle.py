import abc


class Vehicle(abc.ABC):

    _SPEED_LIMIT_WHEN_BREAKDOWN = 75

    def __init__(self, name, normal_speed, distance_traveled):
        self.name = name
        self.normal_speed = normal_speed
        self.distance_traveled = distance_traveled

    @abc.abstractmethod
    def move_for_an_hour(self, race):
        """Moves the vehicle for an hour"""

    @abc.abstractmethod
    def __repr__(self):
        """Prints the information"""
