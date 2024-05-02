# Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favourite_number = {
    "Muhammad": [63, 36],
    "Ali": [57, 75],
    "Fatima": [24, 42],
    "Hassan": [50, 78],
    "Hussain": [45, 54],
}

for name, nums in favourite_number.items():
    print(name + "'s favourite numbers are:")
    for num in nums:
        print(num)
