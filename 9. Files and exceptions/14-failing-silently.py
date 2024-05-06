# Failing silently

# Previously we informed our users that one of the files was unavailable. But you don’t need to report every exception you catch. Sometimes you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened. To make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing in the except block. Python has a "pass" statement that tells it to do nothing in a block


def count_words(filename):
    try:
        with open(filename, encoding="utf-8") as f_obj:
            content = f_obj.read()
    except FileNotFoundError:

        # Addition here
        pass

    else:
        words = content.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


files = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]
for file in files:
    count_words(file)

# In this case no tracback is produced and no error is shown to the user (even the ones that exists)
