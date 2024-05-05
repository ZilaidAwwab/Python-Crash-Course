# Importing an entire module
import car

honda = car.Car("honda", "insight", 2020)
print(honda.get_descriptive_name())

tesla = car.ElectricCar("tesla", "model x", 2023)
print(tesla.get_descriptive_name())
