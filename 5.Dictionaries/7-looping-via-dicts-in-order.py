# Looping though the dictionary’s key in order

# you never get the items from a dictionary in any  predictable order. One way to return items in a certain order is to sort the keys as they’re returned in the for loop. You can use the sorted() function to get a copy of the keys in order

favourite_languages = {
    "Jem": "Perl",
    "Geena": "Objective C",
    "Rossow": "Scala",
    "Zack": "Elixir",
    "Darwin": "Swift",
}

# this returns the sorted result in alphabetical order
for names in sorted(favourite_languages.keys()):
    print(names.title())
