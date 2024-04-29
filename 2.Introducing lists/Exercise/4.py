# . Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.

# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

# Print a message to each of the two people still on your list, letting them know they’re still invited.

# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guest_list = ['Muhammad', 'Ali', 'Hasnain']

print(guest_list[0] + ' is invited on dinner')
print(guest_list[1] + ' is invited on dinner')
print(guest_list[2] + ' is invited on dinner')

print('\nWe have found a bigger dinner table, so now some more guest are invited')

guest_list.insert(0, 'Abu-Bakar')
guest_list.insert(2, 'Umar')
guest_list.append('Usman')

print(guest_list[0] + ' is invited on dinner')
print(guest_list[1] + ' is invited on dinner')
print(guest_list[2] + ' is invited on dinner')
print(guest_list[3] + ' is invited on dinner')
print(guest_list[4] + ' is invited on dinner')
print(guest_list[5] + ' is invited on dinner')

print('\nWe are sorry to announce that we wont be having a big table, and we have to cut down some guests')

uninvited_guest_1 = guest_list.pop()
print(uninvited_guest_1 + 'is not invited on dinner')

uninvited_guest_2 = guest_list.pop()
print(uninvited_guest_2 + 'is not invited on dinner')

uninvited_guest_3 = guest_list.pop()
print(uninvited_guest_3 + 'is not invited on dinner')

uninvited_guest_4 = guest_list.pop()
print(uninvited_guest_4 + 'is not invited on dinner')

print('\nThe invited guests now are:')

print(guest_list[0] + ' is invited on dinner')
print(guest_list[1] + ' is invited on dinner')

del guest_list[1]
del guest_list[0]

print(guest_list)
