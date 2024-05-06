import json


def get_stored_username():
    filename = "username.json"

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("Enter your username: ")
    filename = "username.json"
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you once you come back {username}!")


greet_user()


# Each function in the refactored code has a clear meaning and purposem and thats the purpose of refactoring
