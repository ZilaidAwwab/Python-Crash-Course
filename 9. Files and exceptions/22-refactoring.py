# Refactoring

# Often, you’ll come to a point where your code will work, but you’ll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs. This process is called refactoring. Refactoring makes your code cleaner, easier to understand, and easier to extend.

# Here we will refactor the code that we wrote in the previous program

import json


"""def greet_user():
    filename = "username.json"

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("Enter your username: ")
        with open(filename, "w") as f_obj:
            json.dump(username, f_obj)
            print(f"We'll remember you next time you come back {username}!")
    else:
        print(f"Welcome back {username}!")


greet_user()
"""

# We can further refactor this function


def get_stored_username():
    filename = "username.json"

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}!")
    else:
        username = input("Enter your username: ")
        filename = "username.json"
        with open(filename, "w") as f_obj:
            json.dump(username, f_obj)
            print(f"We'll remember you next time you come back {username}!")


greet_user()

# TIPS:
#  This is good practice: a function should either return the value you’re expecting, or it should return None, as we can see in the get_stored_username function

# We can even further refactor it as we did in the next file
