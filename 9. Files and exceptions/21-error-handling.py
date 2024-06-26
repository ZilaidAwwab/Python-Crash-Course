# Handling errors

import json

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
