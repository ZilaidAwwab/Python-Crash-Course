# Popping items from any position in a list

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)

print('The first motorcycle I owned was ' + first_owned.title() + '.')

# Remember that each time you use pop(), the item you work with is no  longer stored in the list.

# If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.
