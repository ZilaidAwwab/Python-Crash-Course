# Copying a list

# [:] is used to create a slice copy of a list

my_foods = ["pizza", "falafel", "carrot cake"]
friends_food = my_foods[:]

# Now to make sure that these 2 are separate lists, we will add items to both of them
my_foods.append("ice-cream")
friends_food.append("cream rolls")

print("My foods are:")
print(my_foods)

print("\nMy foods are:")
print(friends_food)

# If we had simply set friend_foods equal to my_foods, we would not produce two separate lists
