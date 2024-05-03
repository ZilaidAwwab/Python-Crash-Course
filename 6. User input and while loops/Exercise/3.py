# Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

num = int(input("Enter a number: "))

if num % 10 == 0:
    print("Number " + str(num) + " is a mulitple of 10")
else:
    print("Number " + str(num) + " is not a mulitple of 10")
