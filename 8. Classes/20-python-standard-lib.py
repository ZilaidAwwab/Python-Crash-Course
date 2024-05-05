# The python standard library

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"


# They will be retrieved in the order they are added
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


# We can also download modules from external sources.
