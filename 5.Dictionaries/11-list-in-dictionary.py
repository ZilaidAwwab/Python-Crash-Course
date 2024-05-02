# 	A list in a dictionary
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

print(
    "You have orderd a " + pizza["crust"] + "-crust pizza with the following toppings:"
)

for topping in pizza["toppings"]:
    print("\t" + topping)


# Example
fav_langs = {
    "jen": ["python", "c"],
    "sam": ["perl"],
    "rony": ["scala", "exilir"],
    "zack": ["go", "rust"],
}

for name, languages in fav_langs.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favourite languages are:")
    else:
        print("\n" + name.title() + "'s favourite language is:")

    for lang in languages:
        print(lang)


# try not to nest things very deeply
