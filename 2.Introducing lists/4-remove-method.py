# removing an item by value

# When we dont know the position of the element that we want to remove then we use the remove method and pass the value of the item we want to remove

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


# Another approach
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)

print("\nA " + too_expensive.title() + " is too expensive for me.")

# Here we wanted to use the popped item at some other place that's why we saved it in a variable


#  The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to determine if all occurrences of the value have been removed. You’ll learn how to do this in Chapter 7.
