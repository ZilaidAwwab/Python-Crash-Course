# Working with parts of lists

# Firstly we saw how to access single elements in a list, and in this chapter you’ve been learning how to work through all the elements in a list. You can also work with a specific group of items in a list, which Python calls a slice. To make a slice, you specify the index of the first and last elements you want to work with.

# Here as well the first argument is inclusive and last is exclusive

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])  # ['charles', 'martina', 'michael']

print(players[1:4])  # ['martina', 'michael', 'florence']

print(players[2:])  # ['michael', 'florence', 'eli']

print(players[:4])  # ['charles', 'martina', 'michael', 'florence']

# last 3
print(players[-3:])  # ['michael', 'florence', 'eli']
