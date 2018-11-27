from com.codecool.vehicles.Car import Car
from com.codecool.vehicles.Motorcycle import Motorcycle
from com.codecool.vehicles.Truck import Truck
from com.codecool.weather.Weather import Weather

car = Car()
car2 = Car()
car.move_for_an_hour()
car2.move_for_an_hour()
car2.move_for_an_hour()
print(car)
print(car2)
motor = Motorcycle()
motor2 = Motorcycle()
for i in range(3):
    motor.move_for_an_hour()
print(motor)
print(motor2)
truck = Truck()
truck.move_for_an_hour()
print(truck)

