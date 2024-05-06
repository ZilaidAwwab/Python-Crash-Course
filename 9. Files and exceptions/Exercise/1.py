# You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:

# message = "I really like dogs."
# message.replace('dog', 'cat')
# 'I really like cats.'

filename = "exercise.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.lower().replace("python", "C")
    print(line)
