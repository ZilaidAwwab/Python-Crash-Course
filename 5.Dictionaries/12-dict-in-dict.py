# A dictionary in dictionary

users = {
    "aeinstine": {
        "firstName": "Albert",
        "lastName": "Einstine",
        "location": "Princeton",
    },
    "msurie": {
        "firstName": "Marie",
        "lastName": "Curie",
        "location": "Paris",
    },
}

for userName, details in users.items():
    print("\nUsername: " + userName)
    fullName = details["firstName"] + " " + details["lastName"]
    location = details["location"]

    print("Full Name: " + fullName.title())
    print("Location: " + location.title())
