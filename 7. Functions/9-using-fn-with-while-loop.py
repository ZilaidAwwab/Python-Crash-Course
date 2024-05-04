# 	Using a function with a while loop


def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nEnter your name:")
    print("Press q to quit anytime.\n")

    f_name = input("First Name: ")
    if f_name == "q":
        break

    l_name = input("Last Name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)
