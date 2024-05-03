# Using a while Loop with Lists and Dictionaries

# 	Moving items from one list to another

unconfirmed_users = ["alice", "brian", "mitchell"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying User: " + current_user.title())
    confirmed_users.append(current_user)

print("The following users have been confirmed:")
for user in confirmed_users:
    print(user.title())


# Jus to check
print(unconfirmed_users)
print(confirmed_users)
