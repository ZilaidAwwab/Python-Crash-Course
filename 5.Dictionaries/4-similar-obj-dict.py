# A Dictionary of Similar Objects
# The previous example involved storing different kinds of information about one object, an alien in a game. You can also use a dictionary to store one kind of information about many objects.

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

# Lookup in dictionary

print(
    "Sarah's favourite programming language is: "
    + favorite_languages["sarah"].title()
    + "."
)
