# Polling: Use the code in favorite_languages.py (page 104).

# •	 Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding.If they have not yet taken the poll, print a message inviting them to take the poll

lang_poll = {"Sayem": "Py", "Eric": "C", "Roberts": "Java", "Dennis": "Cpp"}

friends = ["Zim", "Schnider", "Eric", "Dennis"]
for names in friends:
    if names in lang_poll.keys():
        print("Thanks " + names + " for taking the poll!")
    else:
        print(names + " should take the poll!!!")
