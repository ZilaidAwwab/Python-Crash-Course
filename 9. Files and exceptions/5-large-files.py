# Large Files

# Since here we had only 30 digits after a decimal, but we can have more in the real world scenario. Suppose that we have a file with over a million decimal places digits and we just want to print the first 50 digits after decimal, so we can do,

filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

# Here we wrote 52 because 50 digits after the decimal, a decimal and a digit before it
print(pi_string[:52])
print(len(pi_string))
