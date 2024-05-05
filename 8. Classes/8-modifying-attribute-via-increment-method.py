# Modifying attribute through increment method


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

    # addition
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")


my_used_car = Car("BMW", "M4", 2018)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23000)

my_used_car.increment_odometer(1000)
my_used_car.read_odometer()

# We can implement functionalities in the increment method, restricting user to roll back the meter by entering negative values
