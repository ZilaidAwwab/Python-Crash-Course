# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values.When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output

favourite_number = {
    "Muhammad": 63,
    "Ali": 57,
    "Fatima": 24,
    "Hassan": 50,
    "Hussain": 45,
}

for name, age in favourite_number.items():
    print("Favourite Number of " + name + " is " + str(age))
