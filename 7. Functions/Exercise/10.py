# Great Magicians: Start with a copy of your program from Exercise 8-9. Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to see that the list has actually been modified.

magician_names = ["Hymer", "Jemlet", "Cooper", "Zyfer", "Feroh"]


def make_greet(names_list):
    for name in names_list:
        name = f"Great {name}"
        print(name)


make_greet(magician_names[:])
