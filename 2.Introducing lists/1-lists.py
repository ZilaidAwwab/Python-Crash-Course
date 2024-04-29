# Lists & Accessing elements in a list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# we can access any element with its index, along with that we can apply any string method on these items as well
print(bicycles[2].title())
# Redline


# If we want to access the elements from last items, this syntax is quite useful, because you’ll often want to access the last items in a list without knowing  exactly how long the list is.
print(bicycles[-1])
# specialized

print(bicycles[-2])
# redline


# Using individual values from the list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
