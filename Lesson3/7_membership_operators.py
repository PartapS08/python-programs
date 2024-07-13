# Membership operators are in and not in.
# They are used to test whether a value or variable is found in a 
# sequence (string, list, tuple, set, and dictionary).
# The output of these operators is either True or False.

############ in operator ############

# Check if a value is present in a sequence.
a = "Hello World"
print("H" in a)
# Output:
# True

num = [1, 2, 3, 4, 5]
print(10 in num)
# Output:
# False

############ not in operator ############

# Check if a value is not present in a sequence.

a = "Hello World"
print("H" not in a)
# Output:
# False

num = {"Player1": "Rahul", "Player2": "Rohit", "Player3": "Virat"}
print("Sachin" not in num)
# Output:
# True






