# Storing function in modules

# We can go a store oour functions in a separate file called a module and then importing that module into the main program. An import statement tells Python to make the code in a module available in the currently running program file. Storing functions in a separate file allows to hide the details of your program’s code and focus on its higher-level logic. It also allows you to reuse functions in many different programs. When we store functions in separate files, we can share those files with other programmers without having to share your entire program. Knowing how to import functions also allows you to use libraries of functions that other programmers have written.


# Importing an Entire Module

# To start importing functions, we first need to create a module. A module is a file ending in .py that contains the code you want to import into your program. Let’s make a module that contains the function make_pizza().

import pizza

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")
