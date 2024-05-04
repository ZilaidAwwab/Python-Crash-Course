# Default values (or arguments)

# When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value.

# Here a thing to keep in mind is that the parameter with the default argument should be mentioned at the end of parametes list in the function declaration


def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


# Here these both calls output the same results
describe_pet(pet_name="Harry")
describe_pet("Harry")
