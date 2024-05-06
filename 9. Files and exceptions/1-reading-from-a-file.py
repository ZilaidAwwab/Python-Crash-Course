# Reading from a file

# Reading an entire file

# The keyword "with" closes the file once access to it is no longer needed
with open("pi_digits.txt") as file_object:
    contents = file_object.read()

    # Here we are using rstrip to remove the extra whitespaces at the end of the file
    print(contents.rstrip())


# Alternate way (But here we have to close the file manually)
# read_file = open("pi_digits.txt").read()
# print(read_file)


# File path
# We can define the relative path(as described here), or the absolute path(linking the file path that exists anywhere in the machine)
