# Looping through python dictionaries
# A single Python dictionary can contain just a few key-value pairs or millions of pairs. Because a dictionary can contain large amounts of data, Python lets you loop through a dictionary. Dictionaries can be used to store information in a variety of ways; therefore, several different ways exist to loop through them. You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.


# Looping thorugh all key value pairs
user_0 = {
    "username": "cherno",
    "first_name": "chery",
    "last_name": "novan",
}

# here the var names key, values are used only as a indication, although we can use any name here
for key, values in user_0.items():
    print("\nKey: " + key)
    print("Values: " + values)


favourite_languages = {
    "Jem": "Perl",
    "Geena": "Objective C",
    "Rossow": "Scala",
    "Zack": "Elixir",
    "Darwin": "Swift",
}

for names, languages in favourite_languages.items():
    print(names.title() + "'s favourite language is " + languages.title())
