# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"Hello, we are {self.restaurant_name.title()}. Our special cuisine is {self.cuisine_type.title()}."
        )

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["Cheese Cake", "Magnum", "Caramel Crunch"]

    def display_flavours(self):
        print("We have the following flavours:")
        for flavour in self.flavours:
            print(f"\t{flavour}")


# making an instance of the class
omore = IceCreamStand("omore", "deserts")
omore.display_flavours()
