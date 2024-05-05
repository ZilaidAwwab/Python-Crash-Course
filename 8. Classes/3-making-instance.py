class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over")


# Making an instance from class

# Think of a class as a set of instructions for how to make an instance. The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs

# Making instance
my_dog = Dog("willie", 4)


# Accessing attributes
print(f"My Dog's name is {my_dog.name.title()}.")
print(f"My Dog's age is {str(my_dog.age)}.")


# Calling methods

# After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.

my_dog.sit()
my_dog.roll_over()


# Creating multiple instances
your_dog = Dog("lucy", 6)

your_dog.sit()
your_dog.roll_over()

# Even if we used the same name and age for the second dog, Python would still create a separate instance from the Dog class. You can make as many instances from one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary.
