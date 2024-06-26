# Json.dump()

# The json.dump() function takes two arguments: a piece of data to store and a file object it can use to store the data

import json

numbers = [2, 3, 5, 7, 9, 11, 13]

filename = "numbers.json"

with open(filename, "w") as f_obj:
    json.dump(numbers, f_obj)
