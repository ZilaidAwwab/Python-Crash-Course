# 	Handling the File Not Found Error Exception

# One common issue when working with files is handling missing files. The file you’re looking for might be in a different location, the filename may be misspelled, or the file may not exist at all. You can handle all of these situations in a straightforward way with a try-except block.

# Let’s try to read a file that doesn’t exist. The following program tries to read in the contents of Alice in Wonderland, but I haven’t saved the file alice.txt in the same directory as alice.py, so we will use the try except block to handle the situation

filename = "alice.txt"

try:
    with open(filename) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    msg = f"Sorry, the file {filename} doesn't exist"
    print(msg)
