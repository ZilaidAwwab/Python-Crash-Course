# Importing multiple classes from a module

from car import Car, ElectricCar

toyota = Car("toyota", "altis", 2022)
print(toyota.get_descriptive_name())

tesla = ElectricCar("tesla", "roadster", 2021)
print(tesla.get_descriptive_name())
