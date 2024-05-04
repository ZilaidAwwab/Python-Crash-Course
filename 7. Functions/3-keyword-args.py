# Keyword Arguments

# A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion. Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.


def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


# Here the order can be different
describe_pet(animal_type="Hamster", pet_name="Harry")

# They both gives the same output
describe_pet(pet_name="Harry", animal_type="Hamster")
