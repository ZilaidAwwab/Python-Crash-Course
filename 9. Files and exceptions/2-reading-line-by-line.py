# Reading line by line

filename = "pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        # print(line)
        print(line.rstrip())

# With this convention of reading every line of the file, a blank space character is added automatically as the end of every line of the file, so we end up with 2 blank line cahracters and to eliminate it we use the rstrip()
