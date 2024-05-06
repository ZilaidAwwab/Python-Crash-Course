# Storing Data

# We usually want to save the data entered by the user, and we save the data in the json module. The json module allows you to dump simple Python data structures into a file and load the data from that file the next time the program runs. You can also use json to share data between different Python programs. Even better, the JSON data format is not specific to Python, so you can share data you store in the JSON format with people who work in many other programming languages. It’s a useful and portable format, and it’s easy to learn.


# Using json.dump and json.load

# Let’s write a short program that stores a set of numbers and another program that reads these numbers back into memory. The first program will use json.dump() to store the set of numbers, and the second program will use json.load().
