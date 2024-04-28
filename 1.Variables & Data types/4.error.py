# Avoiding Type Errors with the str() Function

age = 21
message = 'Happy ' + str(age) + 'st Birthday'

print(message)

# It is crucial here to add the str function to convert the age variable from int to string in order to concat it with a string, otherwise type error will appear
