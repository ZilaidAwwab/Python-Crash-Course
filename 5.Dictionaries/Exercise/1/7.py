# Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

cat = {
    "kind": "animal",
    "ownerName": "Michael",
}

parrot = {
    "kind": "bird",
    "ownerName": "Clarke",
}

dog = {
    "kind": "animal",
    "ownerName": "Ben",
}

pets = [cat, parrot, dog]

for pet in pets:
    print(
        "\nThis is a kind of " + pet["kind"] + " and its owner is " + pet["ownerName"]
    )
