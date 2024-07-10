# Mapping datatype is Dictionary.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Dictionary is a collection of key:value pairs.
# Empty dictionary is defined as var = {}. here type(var) will return <class 'dict'>.

# ########### dictionary example ############

var = {'name': 'John', 'age': 25, 'grades': [85, 90, 92]}
print(var)
# Output:
# {'name': 'John', 'age': 25, 'height': 5.8, 'married': True}

print("Name:", var['name'])
print("Age:", var['age'])
print("grades:", var['grades'])
# Output:
# Name: John
# Age: 25
# grades: [85, 90, 92]

print("Name:", var.get('name'))
print("Age:", var.get('age'))
print("grades:", var.get('grades'))
# Output:
# Name: John
# Age: 25
# grades: [85, 90, 92]

# In the dictionary if you want to change the value of any element you can do it.
# There are many in-built functions to perform operations on dictionary.
# For example, clear(), copy(), fromkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values() etc.
# Other operations are Membership operators (in, not in), Identity operators (is, is not) etc.

