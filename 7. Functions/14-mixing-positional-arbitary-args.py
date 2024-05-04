# Mixing positional and arbitary arguments

# If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.


def make_pizza(size, *toppings):
    # Adding the loop so to print everything separately
    print(f"Making a {size} inch pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "Pepperoni")
make_pizza(12, "mushrooms", "cheese", "olives")
