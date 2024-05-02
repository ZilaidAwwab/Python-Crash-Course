# Looping through all the keys in a dictionary
favourite_languages = {
    "Jem": "Perl",
    "Geena": "Objective C",
    "Rossow": "Scala",
    "Zack": "Elixir",
    "Darwin": "Swift",
}

for names in favourite_languages.keys():
    print(names.title())


# Same output, but the above one is more self explanatory and better
for names in favourite_languages:
    print(names.title())


friends = ["Geena", "Darwin"]
for names in favourite_languages.keys():
    print(names.title())

    if names in friends:
        print(
            "Hey "
            + names
            + ", I can see your favourite language is "
            + favourite_languages[names].title()
        )

    # Checking if a specific name is present or not
    if "erin" not in favourite_languages:
        print("Erin please take the poll")
