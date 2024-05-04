# Modifying a list in a function

# When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function’s body are permanent, allowing you to work efficiently even when you’re dealing with large amounts of data.


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

print_models(unprinted_designs, completed_models)
competed_models(completed_models)
