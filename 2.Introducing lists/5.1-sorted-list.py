# Sorted

# sorting a list temprarily with sorted function

# To maintain the original order of a list but present it in a sorted order, you  can use the sorted() function. The sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# The sorted function also accepts a reverse=True argument if we want to print the list in reverse order.


# remember that if the list items are not in small case then this sorting might show a different behavior, so in that case we have to make sure that, the case issue is handled first
