# Using arbitrary keyword arguments

# Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information will be passed to the function. In this case, you can write functions that accept as many key-value pairs as the calling statement provides


# The double asteriks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary.
def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile(
    "Albert", "Einstine", location="Princeton", field="Physics"
)
print(user_profile)
