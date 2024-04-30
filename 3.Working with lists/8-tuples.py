# Tuples

# Lists work well for storing sets of items that can change throughout the life of a program. The ability to modify lists is particularly important when you’re working with a list of users on a website or a list of characters in a game. However, sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

# A tuple looks just like a list except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.

dimensions = (200, 500)
print(dimensions[0])  # 200
print(dimensions[1])  # 500

# Not allowed, as they are immutable
# dimensions[0] = 250


# Looping through all values of a tuple
for dimension in dimensions:
    print(dimension)  # 200, 500


# Overwriting tuple
dimensions = (500, 1000)
for dimension in dimensions:
    print(dimension)  # 500, 1000

# this is becasue overwriting a variable is valid

# We should use tuples, when we dont want to change the values of a variable in entire program
