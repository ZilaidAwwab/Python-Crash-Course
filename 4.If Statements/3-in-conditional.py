# checking whether a value is present in the list
toppings = ["mushrooms", "onions", "pineapple"]

print("mushrooms" in toppings)  # true
print("pepperoni" in toppings)  # false


# checking whether a value is not present in the list
banned_users = ["andrew", "caroline", "david"]
user = "marie"

if user not in banned_users:
    print(user.title() + " can post")
