# Looping Through a Slice

# You can use a slice in a for loop if you want to loop through a subset of the elements in a list

players = ["charles", "martina", "michael", "florence", "eli"]

for player in players[:3]:
    print(player.title())
