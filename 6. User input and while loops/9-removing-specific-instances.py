# 	Removing all instances of a specific values from a list

#  We used remove() to remove a specific value from a list. The remove() function worked because the value we were interested in appeared only once in the list. But what if you want to remove all instances of a value from a list? We have a list of pets with the value 'cat' repeated several times. To remove all instances of it, we run a while loop

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)
