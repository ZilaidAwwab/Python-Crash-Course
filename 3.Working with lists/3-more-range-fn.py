# printing the squares of 1-10
squares = []

for val in range(1, 11):
    squares.append(val**2)

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# List compression (performs the same thing as the above code, but in a single line)
compressed_squares = [val**2 for val in range(1, 11)]
print(compressed_squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
