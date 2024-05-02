# Modifying values in a dictionary

alien_0 = {"color": "green"}
print("The alien is " + alien_0["color"] + ".")

alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + ".")


# Advanced modification
alien = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original X-position: " + str(alien["x_position"]))

if alien["speed"] == "slow":
    x_increment = 1
elif alien["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3  # since this is fast

alien["x_position"] += x_increment

print("New X-Position:", alien["x_position"])
