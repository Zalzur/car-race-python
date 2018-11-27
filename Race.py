from com.codecool.vehicles.Car import Car
from com.codecool.vehicles.Motorcycle import Motorcycle
from com.codecool.vehicles.Truck import Truck
from com.codecool.weather.Weather import Weather


class Race:

    __NUMBER_OF_CARS = 10
    __NUMBER_OF_MOTORCYCLES = 10
    __NUMBER_OF_TRUCKS = 10
    __RACE_HOURS = 50

    def __init__(self):
        self.vehicles = []

    def create_vehicles(self):
        for i in range(Race.__NUMBER_OF_CARS):
            self.vehicles.append(Car())
        for i in range(Race.__NUMBER_OF_MOTORCYCLES):
            self.vehicles.append(Motorcycle())
        for i in range(Race.__NUMBER_OF_TRUCKS):
            self.vehicles.append(Truck())

    def simulate_race(self):
        for i in range(Race.__RACE_HOURS):
            Weather.set_raining()
            for j in range(len(self.vehicles)):
                self.vehicles[j].move_for_an_hour(self)

    def print_race_results(self):
        for i in range(len(self.vehicles)):
            if i == 0 or self.vehicles[i].__class__.__name__ != vehicle_type:
                vehicle_type = self.vehicles[i].__class__.__name__
                print("***** " + vehicle_type + "s *****")
            print(self.vehicles[i])

    def is_there_a_broken_truck(self):
        for i in range(len(self.vehicles)):
            if self.vehicles[i].__class__.__name__ == "Truck" and self.vehicles[i].break_down_turns_left > 0:
                return True
        return False


if __name__ == "__main__":
    race = Race()
    race.create_vehicles()
    race.simulate_race()
    race.print_race_results()
