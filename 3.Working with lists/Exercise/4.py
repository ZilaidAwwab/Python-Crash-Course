# Slices: Using one of the programs you wrote in this chapter, add several  lines to the end of the program that do the following:

# •	 Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program’s list.

# •	 Print the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.

# •	 Print the message, The last three items in the list are:. Use a slice to print the last three items in the list

players = ["charles", "martina", "michael", "florence", "eli"]
print("The first 3 players in the list are: ", players[0:3])

print("3 players from the middle of the list are: ", players[1:4])

print("The last 3 players from the list are: ", players[-3:])
