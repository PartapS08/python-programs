# type() is a built-in function in Python that returns the datatype of the object.

########## type() Interger example ###########

# we gonna store the value 10 in the variable 'var' and then run type() function to get the datatype of the variable 'var'
var = 10
type(var) # will get the datatype of the variable 'var'
# No output will be displayed on the console as we are not using print() function to display the output.
print(type(var))
# Output: 
# <class 'int'>

########### type() String example ############

# Remember, vaule with double quotes or single quotes is a string.
var = '10'
print(type(var))
# Output:
# <class 'str'>

########### type() Float example ##############

var = 10.5
print(type(var))
# Output:
# <class 'float'>

########### type() Complex example #############

var = 10 + 5j
print(type(var))
# Output:
# <class 'complex'>

########### type() Boolean example #############

# Boolean data type is used to store 'True' or 'False' values.
# True and False are reserved keywords in Python with the first letter in uppercase.
var = True
print(type(var))
# Output:
# <class 'bool'>

############ type() List example ###############

var = [10, 'Hello', True]
print(type(var))
# Output:
# <class 'list'>

############ type() Tuple example ##############

var = (10, 'Hello', True)
print(type(var))
# Output:
# <class 'tuple'>

############ type() Set example ###############

var = {10, 'Hello', True}
print(type(var))
# Output:
# <class 'set'>

############ type() Range example ###############

var = range(5)
print(type(var))
# Output:
# <class 'range'>

############ type() Dictionary example #########

var = {'name': 'John', 'age': 25}
print(type(var))
# Output:
# <class 'dict'>

############ type() Frozen Set example #########

var = frozenset({10, 'Hello', True})
print(type(var))
# Output:
# <class 'frozenset'>

############ type() Bytes example #############

var = b'Hello'
print(type(var))
# Output:
# <class 'bytes'>

############ type() Byte Array example ########

var = bytearray(5)
print(type(var))
# Output:
# <class 'bytearray'>

############ type() Memory View example ########

var = memoryview(bytes(5))
print(type(var))
# Output:
# <class 'memoryview'>

############ type() None example ###############

var = None
print(type(var))
# Output:
# <class 'NoneType'>
# None is a special constant in Python that represents the absence of a value or a null value.

