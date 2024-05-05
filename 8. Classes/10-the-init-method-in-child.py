# The __init__() Method for a Child Class

# The first task Python has when creating an instance from a child class is to assign values to all attributes in the parent class. To do this, the __init__() method for a child class needs help from its parent class.


# Extending our car class to make an electric car
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


# The name of the parent class must be there in the parenthesis
class ElectricCar(Car):
    # represents aspects of a car, specific to electric car
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_tesla = ElectricCar("tesla", "model s", 2020)
print(my_tesla.get_descriptive_name())

print(my_tesla.odometer_reading)

# The parent class must be before the child class in the file

# The super() function is a special function that helps Python make connections between the parent and child class. This line tells Python to call the __init__() method from parent class, which gives the child class instance all the attributes of its parent class. The name supercomes from a convention of calling the parent class a superclass and the child class a subclass.
