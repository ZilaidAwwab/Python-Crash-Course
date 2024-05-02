#  Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favourite_places = {
    "Faiq": "Miami",
    "Armaan": "Seatle",
    "Zikria": "California",
}

for name, place in favourite_places.items():
    print(name.title() + "'s favourite place is " + place.title())
