# Using "as" to give function as Alias

# If the name of a function you’re importing might conflict with an existing name in your program or if the function name is long, you can use a short, unique alias—an alternate name similar to a nickname for the function. You’ll give the function this special nickname when you import the function

from pizza import make_pizza as mp

mp(16, "Pepperoni", "Olives", "Mushrooms")
