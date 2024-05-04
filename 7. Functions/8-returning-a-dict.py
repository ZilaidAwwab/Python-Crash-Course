# Returning a dictionary

# A function can return any kind of value including more complicated data structures like lists and dictionaries.


def build_person(first_name, last_name, age=""):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


profile = build_person("Zilaid", "Awwab", 21)
print(profile)
