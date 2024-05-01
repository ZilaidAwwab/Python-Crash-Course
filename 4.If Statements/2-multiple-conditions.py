# If we want both conditions to be true, we use 'and'

height = 6.0
weight = 72

if height >= 5.10 and weight >= 70:
    print("Eligible")
else:
    print("Not eligible")


# If we want either or both conditions to be true, we use 'or'
if height >= 6.0 or weight >= 75:
    print("Criteria passed")
else:
    print("Criteria failed")
