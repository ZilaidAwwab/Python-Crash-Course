#  Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

# •	 Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary

rivers = {
    "China": "Tigris",
    "Pakistan": "Indus",
    "India": "Ganges",
}

for country, river in rivers.items():
    print(river + " runs through " + country)

for only_river in rivers.values():
    print(only_river.title())

for only_country in rivers.keys():
    print(country.title())
