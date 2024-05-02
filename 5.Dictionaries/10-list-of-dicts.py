# Expanding the last file we can dynamically create aliens as well

aliens = []

for alien in range(30):
    new_alien = {"color": "red", "points": 10, "speed": "medium"}
    aliens.append(new_alien)


# Changing the attributes of first 3 aliens
for alien in aliens[0:3]:
    if alien["color"] == "red":
        alien["color"] = "yellow"
        alien["points"] = 15
        alien["speed"] = "fast"

# printing the first 5 items
for alien in aliens[:5]:
    print(alien)

print("Total number of aliens are: " + str(len(aliens)))  # 30
