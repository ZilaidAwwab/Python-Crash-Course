# Using break to exit the loop

# To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished.\n"

while True:
    city = input(prompt)

    if city == "quit":
        break
    print("I would love to go to " + city.title())

# A loop that starts with while True u will run forever unless it reaches a break statement.

# You can use the break statement in any of Python’s loops. For example, you could use break to quit a for loop that’s working through a list or a dictionary.
