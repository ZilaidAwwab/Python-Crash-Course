# Defining attributes and methods for the child class

# Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back the meter")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def decsribe_battery(self):
        print(f"This car has a {str(self.battery_size)}-KWh battery size")


my_tesla = ElectricCar("tesla", "model s", 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery_size = 120
my_tesla.decsribe_battery()
