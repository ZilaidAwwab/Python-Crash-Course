# Defining a function


def greet_user():
    """Displays a simple display message"""
    print("Hello!")


greet_user()


# Passing information to the function (arguments)
def greeting_user(username):
    print("Hello", username.title())


greeting_user("Zilaid")


# Parameters and Arguments
# Parameter is the piece of information that the function needs to do its job (here the variable "username" is example of a parameter)

# Argument is the piece of information passed from a function call to the function (here "Zilaid" is example of argument)
