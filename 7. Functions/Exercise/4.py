#  Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


def make_shirt(size="large", text="I Love Python"):
    print(f"Your shirt is of {size} size, with a text {text} written over it.")


make_shirt()
make_shirt("medium")
make_shirt(size="medium", text="Gucci")
