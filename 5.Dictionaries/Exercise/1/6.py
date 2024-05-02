# People: Start with the program you wrote for Exercise 6-1 (page 102). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person

person1 = {
    "first_name": "Muhammad",
    "last_name": "Abdullah",
    "age": 63,
    "city": "Madina",
}

person2 = {
    "first_name": "Ali",
    "last_name": "Abu Talib",
    "age": 60,
    "city": "Kufa",
}

person3 = {
    "first_name": "Hussain",
    "last_name": "Ali",
    "age": 50,
    "city": "Syria",
}

people = [person1, person2, person3]

for person in people:
    print(
        "He is "
        + person["first_name"]
        + " "
        + person["last_name"]
        + ". His age is "
        + str(person["age"])
        + " and he lives in "
        + person["city"]
        + "."
    )
