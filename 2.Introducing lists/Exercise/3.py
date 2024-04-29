# . More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end of your program informing people that you found a bigger dinner table.

# Use insert() to add one new guest to the beginning of your list.

# Use insert() to add one new guest to the middle of your list.

# Use append() to add one new guest to the end of your list.

# Print a new set of invitation messages, one for each person in your list.

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
