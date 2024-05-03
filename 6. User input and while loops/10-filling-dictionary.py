# 	Filling a dictionary with user input

responses = {}

polling_active = True

while polling_active:
    name = input("What's your name:\n")
    response = input("\nWhich mountain you'd like to climb:\n")

    responses[name] = response

    repeat = input("Do you want to add data for someone else. (yes/no): ")

    if repeat == "no":
        polling_active = False

print("Printing Results...")
for name, response in responses.items():
    print(name.title() + " will like to climb " + response.title() + " mountain.")
