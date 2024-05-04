# Unchanged Magicians: Start with your work from Exercise 8-10. Call the function make_great() with a copy of the list of magicians’ names. Because the original list will be unchanged, return the new list and store it in a separate list.Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.

magician_names = ["Hymer", "Jemlet", "Cooper", "Zyfer", "Feroh"]

new_magician_list = []


def make_greet(names_list):
    for name in names_list:
        name = f"Great {name}"
        print(name)

        new_magician_list.append(name)


make_greet(magician_names[:])

print(magician_names)
print(new_magician_list)
