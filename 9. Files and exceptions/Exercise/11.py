# Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.

import json


def display_fav_num():
    filename = "favourite.json"
    try:
        with open(filename, "r") as f_obj:
            fav_number = json.load(f_obj)
    except FileNotFoundError:
        return fav_number
    else:
        return fav_number


def get_favourite_num():
    filename = "favourite.json"
    fav_number = input("Enter you favourite number: ")
    with open(filename, "w") as f_obj:
        json.dump(fav_number, f_obj)
        return fav_number


def fav_num():
    fav_num = display_fav_num()
    if fav_num:
        print(f"We know your favourite number is {fav_num}")
    else:
        fav_num = get_favourite_num()
        print(f"Your favourite number {fav_num} is stored in the file")


fav_num()
