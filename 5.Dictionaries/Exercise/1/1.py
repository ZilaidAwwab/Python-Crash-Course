# Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

person = {
    "first_name": "Muhammad",
    "last_name": "Abdullah",
    "age": 63,
    "city": "Madina",
}

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
