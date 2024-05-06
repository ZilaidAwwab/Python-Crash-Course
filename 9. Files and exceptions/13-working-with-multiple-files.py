# Working with multiple files

# To find the info regarding multiple files we need to make a function that can in take the file name and return the number of words in it


def count_words(filename):
    try:
        with open(filename, encoding="utf-8") as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        msg = f"{filename} doesn't exist"
        print(msg)
    else:
        words = content.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


# count_words("alice.txt")

# Now we will keep the file names in the array and then run the loop so that we can get the words in each file in a go, we will also check the efficiency of the program by keeping a file name that dont exist, so that we can see the error msg

files = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]
for file in files:
    count_words(file)
