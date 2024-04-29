motorcycles = ['Honda', 'Yamaha', 'Suzuki']

# Removing

# removing element from the list
# 'if we know the location of the element we can use del, this is a permanent operation and we cannot access the removed element after it is deleted'
del motorcycles[3]
print(motorcycles)


# removing (pop)
# 'The pop() method removes the last item in a list, but it lets you work with that item after removing it'
motorcycles.pop()
print(motorcycles)

# We can store the popped element in another variable and can use it later, as we will require in some cases.
popped_motorcycle = motorcycles.pop()
print(motorcycles)

print(popped_motorcycle)
