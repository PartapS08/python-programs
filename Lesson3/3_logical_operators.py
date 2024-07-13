# Logical Operators are 'and', 'or', 'not'. Check Readme.md
# Logical operators are used to combine multiple conditions and return a boolean value (True or False).
# Mostly used in conditional statements like if, if-else.
# Precedence of Logical Operators: 'not' > 'and' > 'or'

########## 'and' Operator Example ##########

a = 10
b = 20
c = 30
result = a < b and b < c
print("a < b and b < c is", result)
# Output:
# a < b and b < c is True

# and operator returns True if both conditions are True, otherwise False.

########## 'or' Operator Example ##########

a = 10
b = 20
c = 30
result = a < b or b > c
print("a < b or b > c is", result)
# Output:
# a < b or b > c is True

# or operator returns True if any one of the conditions is True, otherwise False.

########## 'not' Operator Example ##########

a = 10
b = 20
result = not a < b
print("not a < b is", result)
# Output:
# not a < b is False

# not operator returns True if the condition is False, otherwise False.

# Combining Logical Operators

a = 10
b = 20
c = 30
result = not a < b and b < c
print("not a < b and b < c is", result)
# Output:
# not a < b and b < c is False

result = not True or False and True  
print(result)
# Output:
# False 
#because 'not' has the highest precedence, followed by and, then or
