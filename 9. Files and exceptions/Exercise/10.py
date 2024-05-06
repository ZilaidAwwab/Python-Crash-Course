# Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”

import json


def favourite_num():
    filename = "favourite.json"
    fav_number = input("Enter you favourite number: ")
    with open(filename, "w") as f_obj:
        json.dump(fav_number, f_obj)
        print(f"Your favourite number {fav_number} is stored in the file")


favourite_num()
