# None datatype is used to define a null value or no value at all. 
# It is not same as 0 or False.
# None can be defined as var = None. Here type(var) will return <class 'NoneType'>.
# None is a keyword in Python with the first letter in uppercase.

var = None
print(type(var))
# Output:
# <class 'NoneType'>

############ None example ############

name = input("Enter your name: ")
if name == None:
    print("You didn't enter your name.")
# Output:
# Enter your name:
# You didn't enter your name.


