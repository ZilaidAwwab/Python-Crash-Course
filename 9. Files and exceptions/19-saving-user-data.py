# Saving and reading user generated data

import json

username = input("Enter you name: ")

filename = "username.json"

with open(filename, "w") as f_obj:
    json.dump(username, f_obj)
    print(f"We'll save your name for the next time {username.title()}!")
