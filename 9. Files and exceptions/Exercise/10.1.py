import json

filename = "favourite.json"


def display_fav_num():
    with open(filename, "r") as f_obj:
        fav_number = json.load(f_obj)
        print(f"We know your favourite number is {fav_number}")


display_fav_num()
