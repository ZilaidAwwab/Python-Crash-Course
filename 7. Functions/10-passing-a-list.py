# Passing a list


def greet(names):
    for name in names:
        msg = f"Hello, {name}!"
        print(msg)


names_list = ["Abuzar", "Miqdad", "Salman"]
greet(names_list)
