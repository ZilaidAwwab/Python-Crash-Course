from name_function import get_formatted_name

print("Press 'q' to exit the function at any place.\n")

while True:
    first = input("Enter your first name: ")
    if first == "q":
        break
    last = input("Enter your last name: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print("The full name of the user is: " + formatted_name)
