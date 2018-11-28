import unittest

from com.codecool.vehicles.Car import Car
from com.codecool.vehicles.Motorcycle import Motorcycle
from com.codecool.vehicles.Truck import Truck


class RaceTest(unittest.TestCase):

    cars = []
    motorcycles = []
    trucks = []

    for i in range(10):
        cars.append(Car())
        motorcycles.append(Motorcycle())
        trucks.append(Truck())

    def test_car_names(self):
        car_names = []
        car_name_list = ["Prime", "Marvel", "Pinnacle", "Chase", "Renegade",
                         "Ethereal", "Legend", "Guardian", "Vertex", "Encounter"]
        for i in range(len(self.cars)):
            car_names += self.cars[i].name.split(' ')
            self.assertTrue(car_names[i] in car_name_list)

    def test_car_max_speed(self):
        max_speed = 110
        for i in range(len(self.cars)):
            self.assertLessEqual(self.cars[i].normal_speed, max_speed)

    def test_car_min_speed(self):
        min_speed = 80
        for i in range(len(self.cars)):
            self.assertGreaterEqual(self.cars[i].normal_speed, min_speed)

    def test_motorcycles_name(self):
        names = ["Motorcycle 1", "Motorcycle 2", "Motorcycle 3", "Motorcycle 4", "Motorcycle 5",
                 "Motorcycle 6", "Motorcycle 7", "Motorcycle 8", "Motorcycle 9", "Motorcycle 10"]
        for i in range(len(self.motorcycles)):
            self.assertEqual(self.motorcycles[i].name, names[i])

    def test_motorcycles_speed(self):
        speed = 100
        for i in range(len(self.motorcycles)):
            self.assertEqual(self.motorcycles[i].normal_speed, speed)

    def test_motorcycles_rain_min_speed(self):
        rain_min_speed = 50
        for i in range(len(self.motorcycles)):
            self.assertGreaterEqual(self.motorcycles[i].rain_speed, rain_min_speed)

    def test_motorcycles_rain_max_speed(self):
        rain_min_speed = 95
        for i in range(len(self.motorcycles)):
            self.assertLessEqual(self.motorcycles[i].rain_speed, rain_min_speed)



