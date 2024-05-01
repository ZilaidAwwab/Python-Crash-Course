# Using if statements with lists

# Checking for special condition
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for toppings in requested_toppings:
    if toppings == "green peppers":
        print("Sorry, we are out of green peppers right now")
    else:
        print("Adding " + toppings + ".")

print("\nFinished making your pizza")


# Checking that list is not empty
pizza_toppings = []

if pizza_toppings:
    for topping in pizza_toppings:
        print("Adding " + topping + ".")
    print("Finished adding toppings")

else:
    print("Are you sure, not to add toppings")
