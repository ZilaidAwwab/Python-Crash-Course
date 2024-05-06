# Working with file's content

# After you’ve read a file into memory, you can do whatever you want with that data, so let’s briefly explore the digits of pi. First, we’ll attempt to build a single string containing all the digits in the file with no whitespace in it

filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    # this removes only the whitespaces at the right
    # pi_string += line.rstrip()

    # if we want to remove spaces from all over then we use strip
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value in a numerical context, you’ll have to convert it to an integer using the int() function or convert it to a float using the float() function
