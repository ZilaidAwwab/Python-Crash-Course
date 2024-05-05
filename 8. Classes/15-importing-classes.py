# Importing classes

# As you add more functionality to your classes, your files can get long, even when you use inheritance properly. In keeping with the overall philosophy of Python, you’ll want to keep your files as uncluttered as possible. To help, Python lets you store classes in modules and then import the classes you need into your main program.


# Importing a single class
from car import Car

my_new_car = Car("mercedes", "c150", 2022)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 2000
my_new_car.read_odometer()


# Storing multiple classes in a module

# You can store as many classes as you need in a single module, although each class in a module should be related somehow. The classes Battery and ElectricCar both help represent cars, so let’s add them to the module car.py

from car import ElectricCar

tesla = ElectricCar("tesla", "model s", 2021)
print(tesla.get_descriptive_name())

tesla.battery.describe_battery()
tesla.battery.get_range()
