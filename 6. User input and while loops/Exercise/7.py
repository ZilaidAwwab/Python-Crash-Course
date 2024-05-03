#  No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Filled", "Pastrami", "Vegetable", "Chicken", "Pastrami"]
finished_sandwhiches = []

print("Deli has run out of Pastrami")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    current_sandwhich = sandwich_orders.pop()

    print("I made your " + current_sandwhich + " sandwhich")

    finished_sandwhiches.append(current_sandwhich)

print("Completed...")
for sandwhiches in finished_sandwhiches:
    print(sandwhiches + " sandwhich was delievered")

# Confirmation
print(sandwich_orders)
print(finished_sandwhiches)
