# Instances as attributes

# When modeling something from the real world in code, you may find that you’re adding more and more detail to a class. You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy. In these situations, you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together.

# For example, if we continue adding detail to the ElectricCar class, we might notice that we’re adding many attributes and methods specific to the car’s battery. When we see this happening, we can stop and move those attributes and methods to a separate class called Battery. Then we can use a Battery instance as an attribute in the ElectricCar class:


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


# Adding a class that will become an instance of the existing class
class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {str(self.battery_size)}-KWh battery.")

    # Now here we have a separate class for an instance so we can expand this to any level we want without thinking of making the code spegetti code
    def get_range(self):
        if self.battery_size <= 70:
            range = 240
        elif self.battery_size >= 85:
            range = 300

        message = f"This car can go approximately {str(range)} miles on a full charge"
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        # There we created Battery class instance as an attribue inside the main class
        self.battery = Battery()


tesla = ElectricCar("telsa", "model x", 2022)

# consuming the changes
tesla.battery.describe_battery()

# as there's an optional parameter in the battery class so here we can consume that as well
tesla.battery.battery_size = 100
tesla.battery.describe_battery()

tesla.battery.get_range()
