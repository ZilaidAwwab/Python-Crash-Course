#  Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    "Michigan": {
        "country": "States",
        "population": "2 Million",
        "fact": "Dr Chuck",
    },
    "Miami": {
        "country": "States",
        "population": "3 Million",
        "fact": "Stunning Beaches",
    },
    "California": {
        "country": "States",
        "population": "1 Million",
        "fact": "Silicon Valley",
    },
}

for city, facts in cities.items():
    print(
        "Talking about " + city,
        ". It is located in",
        facts["country"],
        "and it's population is ",
        facts["population"],
        " and its special item is ",
        facts["fact"],
    )
