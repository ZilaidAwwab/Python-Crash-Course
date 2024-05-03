# Writing clean input prompts messages

# We should split the prompt on multiple lines if it is long

prompt = "If you can tell us your name, then we can message you personally."
prompt += "\nWhat is your name?: "

name = input(prompt)
print("Hello", name)


# Using int to accept numerical input
age = int(input("Enter your age: "))
if age > 18:
    print("Eligiblity for Vote found")
else:
    print("Not eligible to vote")
