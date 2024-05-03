# Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza

prompt = "Enter the toppings you want on your pizza:\n"

while True:
    toppings = input(prompt)

    if toppings == "quit":
        break

    print("You'll add " + toppings.title() + " to your pizza")
