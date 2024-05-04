# 	Passing an arbitrary number of arguments

# Sometimes you won’t know ahead of time how many arguments a function needs to accept. Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.

#  Here this "*toppings" parameter collects as many arguments as the calling line provides


def make_pizza(*toppings):
    # Adding the loop so to print everything separately
    print("Making a pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("Pepperoni")
make_pizza("mushrooms", "cheese", "olives")

# Before adding loop
# ('Pepperoni',)
# ('mushrooms', 'cheese', 'olives')


# The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever values it receives
