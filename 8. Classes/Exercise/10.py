# OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you used a standard dictionary to represent a glossary. Rewrite the program using the OrderedDict class and make sure the order of the output matches the order in which key-value pairs were added to the dictionary.

from collections import OrderedDict

favourite_number = OrderedDict()

favourite_number["Muhammad"] = 63
favourite_number["Ali"] = 57
favourite_number["Fatima"] = 24
favourite_number["Hassan"] = 50
favourite_number["Hussain"] = 45

for name, age in favourite_number.items():
    print("Favourite Number of " + name + " is " + str(age))
