# Using exceptions to prevent crashes

# Here we are doing simple division and wrapping the part of code inside the try-except block where the traceback errors can occour incase user input some information not appropriate

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
