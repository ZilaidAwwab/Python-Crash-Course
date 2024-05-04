# Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.


def make_sandwhich(*items):
    print("Your sandwhich will contain these items:")
    for item in items:
        print(f"- {item}")


make_sandwhich("Vegetable")
make_sandwhich("Chillies", "Mayoneese", "Pepper")
make_sandwhich("Sauce", "Garlics")
