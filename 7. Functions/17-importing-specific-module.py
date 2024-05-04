# Importing speicfic functions

# The syntax for this is,
# from module_name import function_name

# You can import as many functions as you want from a module by separating each function’s name with a comma:

from pizza import make_pizza

# Now to use the function, we don't need the module name precedence

make_pizza(13, "Pepperoni", "Olives")
