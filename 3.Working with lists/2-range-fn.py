# making numerical lists

# In range function, the first argument is inclusive and second is exclusive (called off-by-one behavior)
for value in range(1, 5):
    print(value)  # 1-4


# using range() to make a list of numbers
numbers = list(range(1, 10))
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# We can also use the range() function to tell Python to skip numbers in a given range. For example, here’s how we would list the even numbers between 1 and 18:
even_numbers = list(range(2, 19, 2))
print(even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18]
