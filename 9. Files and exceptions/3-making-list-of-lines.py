# Making a list of lines from a file

# When you use with, the file object returned by open() is only available inside the with block that contains it. If you want to retain access to a file’s contents outside the with block, you can store the file’s lines in a list inside the block and then work with that list.

filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
