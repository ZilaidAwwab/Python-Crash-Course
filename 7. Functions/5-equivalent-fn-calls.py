# Equivalent function calls

# We know that there could be serveral ways of describing a function (with and without default values), moreover there are also several ways of calling the function, positional and keyword argument (in or not in order). So, here we will just have a overview of all of them


def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


# There are 5 ways of calling this function
describe_pet("Harry")
describe_pet(pet_name="Harry")

describe_pet("Harry", "Hamster")
describe_pet(animal_type="Hamster", pet_name="Harry")
describe_pet(pet_name="Harry", animal_type="Hamster")
