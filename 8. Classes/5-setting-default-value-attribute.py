# Setting a default value for attribute

# Every attribute in a class needs an initial value, even if that value is 0 or an empty string. In some cases, such as when setting a default value, it makes sense to specify this initial value in the body of the __init__() method; if you do this for an attribute, you don’t have to include a parameter for that attribute

# We will add an attribute called odometer_reading that always starts with a value of 0. We’ll also add a method read_odometer() that helps us read each car’s odometer:


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        # addition
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()

    # addition
    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")


my_new_car = Car("audi", "a8", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
