cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# The equality check (==), is case sensative check

request_toppings = "mushrooms"

if request_toppings != "anchovies":
    print("Hold the anchovies")


# other comparison operators like <, >, <=, >= can also be used in conditional checking


# if-elif-else
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# OMITTING THE ELSE
# We are not restricted to use else block must, we can just skip that and handle all the possible conditions with elif


# MULTIPLE IF STATEMENTS
# sometimes it’s important to check all of the conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks. This technique makes sense when more than one condition could be True, and you want to act on every condition that is True
