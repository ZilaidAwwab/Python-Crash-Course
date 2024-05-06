# Is you birthday appears in the file

filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday in mmddyy:\n")

if birthday in pi_string:
    print("Your birthday exists in the file!")
else:
    print("Your birthday doesn't exist in the file!")
