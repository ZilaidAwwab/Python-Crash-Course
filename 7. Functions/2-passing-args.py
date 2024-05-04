# Passing Arguments

# A function definition can have multiple parameters, a function call may need multiple arguments. You can pass arguments to your functions in a number of ways. You can use "positional arguments", which need to be in the same order the parameters were written; "keyword arguments", where each argument consists of a variable name and a value; and lists and dictionaries of values. Let’s look at each of these in turn.


# Positional Arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


describe_pet("Hamster", "Harry")


# Multiple function calls
# (We can call the defined function as many times as we want)
describe_pet("German Shepherd", "Sherfo")
describe_pet("Labra Dor", "Micky")


# Order (of arguments )matters in positional arguments
