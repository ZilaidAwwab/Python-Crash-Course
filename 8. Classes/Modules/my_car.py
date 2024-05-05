from car import Car
from electric_car import ElectricCar

kia = Car("kia", "sportage", 2023)
print(kia.get_descriptive_name())

toyota = ElectricCar("toyota", "prius", 2021)
print(toyota.get_descriptive_name())
