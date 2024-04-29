# Avoiding Index Errors When Working with Lists

# We should remember that index in the list starts at 0. So, Keep in mind that whenever you want to access the last item in a list  you use the index -1. This will always work, even if your list has changed size since the last time you accessed it

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

# The only time this approach will cause an error is when you request the  last item from an empty list:

motorcycles = [] 
print(motorcycles[-1])

# If an index error occurs and you can’t figure out how to resolve it, try printing your list or just printing the length of your list. Your list might look much different than you thought it did, especially if it has been managed dynamically by your program. Seeing the actual list, or the exact number of items in your list, can help you sort out such logical errors
