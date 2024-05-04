# Preventing the function from modifying the list

# In the previous example we saw that the function modified our original list to populate the other one but, Sometimes we want to keep the original list unchanged, and to achieve this we pass the copy of the original list to the function rather than the original list

# The slice makes the copy of the list and sent this to the function
# function_name(list_name[:])


# rewriting the previous program code
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Design: {current_design}")
        completed_models.append(current_design)


def competed_models(completed_models):
    print("The following models have been printed")
    for model in completed_models:
        print(model)


unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

# Here we used the slice convention
print_models(unprinted_designs[:], completed_models)
competed_models(completed_models)

# Even though you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions unless you have a specific reason to pass a copy. It’s more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially when you’re working with large lists.
