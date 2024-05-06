# Analyzing text (using split method)

# The split() method separates a string into parts wherever it finds a space and stores all the parts of the string in a list. The result is a list of words from the string, although some punctuation may also appear with some of the words. To count the number of words in Alice in Wonderland, we’ll use split() on the entire text.

# Here we are counting the number of words in a file

filename = "alice.txt"

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
