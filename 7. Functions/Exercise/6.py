# City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:

# "Santiago, Chile"

# Call your function with at least three city-country pairs, and print the value that’s returned.


def city_country(city, country):
    full_name = f"{city}, {country}"
    return full_name.title()


print(city_country("paris", "france"))
print(city_country("barcelona", "spain"))
print(city_country("liverpool", "england"))
