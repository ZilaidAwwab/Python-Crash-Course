# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

# Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.


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


# creating instance
restaurant = Restaurant("Malako", "Russian Cuisine")

# printing attributes
print(f"{restaurant.restaurant_name.title()}")
print(f"{restaurant.cuisine_type.title()}")

# calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()


# making other instances and calling methods
fav_restaurant = Restaurant("Otpt", "Frizza")
fav_restaurant.describe_restaurant()
