# Overdiding methods from the parent class

# You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class. To do this, you define a method in the child class with the "same name" as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.

# Say the class Car had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle, so you might want to override this method.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def fill_gas_tank(self):
        print("This has a 55 litres of gas tank")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    # We wanted to override this method from the parent class, so we used the same name as it was used in the parent class
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank")


tesla = ElectricCar("tesla", "model z", 2021)
tesla.fill_gas_tank()

# Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method fill_gas_tank() in Car and run this code instead. When you use inheritance, you can make your child classes retain what you need and override anything you don’t need from the parent class
