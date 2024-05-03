# Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

vacation = {}

prompt1 = "What is your name?\n"
prompt2 = "If you could visit one place in the world, what would that be?\n"
prompt3 = "Do you want to enter data for someone else (yes/no): "

poll_active = True

while poll_active:
    name = input(prompt1)
    place = input(prompt2)

    vacation[name] = place

    repeat = input(prompt3)

    if repeat == "no":
        break

print("Printing the poll result...")
for name, place in vacation.items():
    print(name.title() + " would like to visit " + place.title())
