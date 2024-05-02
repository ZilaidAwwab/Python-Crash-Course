# Looping Through All Values in a Dictionary

favourite_languages = {
    "Jem": "Perl",
    "Geena": "Elixir",
    "Rossow": "Scala",
    "Zack": "Elixir",
    "Darwin": "Swift",
}

print("The following languages are mentioned")
for names in favourite_languages.values():
    print(names.title())
# This appraoch even print the repeated values, and if we just want to pick unique then we use sets


# SET
# A set is similar to a list except that each item in the set must be unique
print("\nThe following unique languages are mentioned")
for names in set(favourite_languages.values()):
    print(names.title())
