# Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

print("This program adds the number you provide")
print("Press q to quit the program")

while True:
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
    except ValueError:
        print("Enter a valid number")

    else:
        sums = number1 + number2
        print(sums)
