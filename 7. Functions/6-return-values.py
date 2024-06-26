# Return Values

# A function doesn’t always have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function. Return values allow you to move much of your program’s grunt work into functions, which can simplify the body of your program.


# returning a simple value
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


# The returned value from the function needs to be stored in a variable, that's why we have created one here
musician = get_formatted_name("elicia", "borne")
print(musician)
