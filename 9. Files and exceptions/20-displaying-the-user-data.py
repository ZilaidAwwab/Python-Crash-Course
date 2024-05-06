# Displaying the data saved of the user in the file

import json

filename = "username.json"

with open(filename) as f_obj:
    username = json.load(f_obj)
    print(f"Welcome back {username}!")
