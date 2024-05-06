# Programming Poll: Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

filename = "program_reason.txt"

while True:
    reason = input("Why you love Programming:\n")
    if reason == "quit":
        break
    else:
        with open(filename, "a") as file_object:
            file_object.write(reason + "\n")
