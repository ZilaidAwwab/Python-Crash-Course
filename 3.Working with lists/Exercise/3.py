# Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for nums in range(1, 21):
    print(nums)


# printing the stats for list
numbers = list(range(1, 100))

print(min(numbers))  # 1
print(max(numbers))  # 99
print(sum(numbers))  # 4950


# 3rd argument to print the odd numbers
odd_numbers = [val for val in range(1, 20, 2)]
print(odd_numbers)


# Make a list of the multiples of 3 from 3 to 30
multiples = [val * 3 for val in range(3, 30)]
print(multiples)


# Use a list comprehension to generate a list of the first 10 cubes
cubes = [val**3 for val in range(1, 11)]
print(cubes)
