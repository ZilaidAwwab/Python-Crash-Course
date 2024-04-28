# Stripping whitespaces

# removing spaces from the right
fav_lang = 'Python '
print(fav_lang.rstrip()) # 'Python'


# removing spaces from the left
oth_fav = ' JavaScript'
print(oth_fav.lstrip()) # 'JavaScript'


# removing spaces from the right and left both
most_fav = ' Urdu '
print(most_fav.strip()) # 'Urdu'


# A thing to note here is that these are the temporary changes to the actual variable names. if we want to permanently change the value then we have to store then in a separate variable like,

fav_lang = fav_lang.rstrip()
print(fav_lang) # 'Python'
