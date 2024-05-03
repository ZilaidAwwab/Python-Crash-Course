# 	The modulo operator
# It divides one number by another number and returns the remainder

number = int(input("Enter a number and I will tell you whether it is even or odd: "))

if number % 2 == 0:
    print("The number " + str(number) + " is even")
else:
    print("The number " + str(number) + " is odd")
