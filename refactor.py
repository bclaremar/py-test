# assign-if-exp
condition = True
if condition:
    x = 1
else:
    x = 2


# Augmented assign
count = 2
other_value = 2
count = count + other_value


# Chain compares
b = 2
if 1 < b and b < 3:
    print("b is between 1 and 3")


# convert-any-to-in
hats = ["basker", "cap", "bowler"]
if any(hat == "bowler" for hat in hats):
    print("I have a bowler hat!")

