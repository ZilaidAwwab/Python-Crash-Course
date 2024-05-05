# Working with classes and instances

# You can use classes to represent many real-world situations. Once you write a class, you’ll spend most of your time working with instances created from that class. One of the first tasks you’ll want to do is modify the attributes associated with a particular instance. You can modify the attributes of an instance directly or write methods that update attributes in specific ways.


# A simple class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a8", 2024)
print(my_new_car.get_descriptive_name())
