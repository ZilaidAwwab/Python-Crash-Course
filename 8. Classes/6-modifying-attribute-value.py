# 	Modifying attribute values

# You can change an attribute’s value in three ways: you can change the value directly through an instance, set the value through a method, or increment the value (add a certain amount to it) through a method.

# Modifying attribute value directly

# The simplest method is to access the attribute directly through the instance


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")


my_new_car = Car("audi", "a8", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
