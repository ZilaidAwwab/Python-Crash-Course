# Modifying attribute value through method


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()

    # addition
    def update_odometer(self, milage):
        # extending the functionality of this odometer function, by rejecting the change if someone tries to rollback the odometer
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back the meter")

    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")


my_new_car = Car("audi", "a8", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Checking the condition added in the update method
my_new_car.update_odometer(10)
my_new_car.read_odometer()
