# In python, we can define a function with def keyword.
# Syntax: def function_name(parameters):

def greet():
    print('Hello, welcome to Python programming')

# Call the function
greet()
# Output:
# Hello, welcome to Python programming

# So, we use function to perform a specific task and reuse it whenever required.

############ function example ############

# Calculator
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

# Call the functions
# Now anytime we need to perform addition, subtraction, multiplication or division, 
# we can call these functions and dont need to write the code a+b or a-b again.

print(add(10, 20))  # Output: 30
print(subtract(20, 10))  # Output: 10
print(multiply(10, 20))  # Output: 200
print(divide(20, 10))  # Output: 2.0

############ function with arguments ############

# Positional arguments
# Keyword arguments
# Default arguments
# Variable-length arguments

# Positional arguments
def greet(name, message):
    print(f"Hello {name}, {message}")

# Call the function
greet('John', 'welcome to Python programming')
# Output:
# Hello John, welcome to Python programming

# Keyword arguments
def greet(name, message):
    print(f"Hello {name}, {message}")
    
# Call the function
greet(message='welcome to Python programming', name='John')
# Output:
# Hello John, welcome to Python programming

# Default arguments
def greet(name, message='welcome to Python programming'):
    print(f"Hello {name}, {message}")

# Call the function
greet('John')
# Output:
# Hello John, welcome to Python programming

# Variable-length arguments
def greet(*names):
    for name in names:
        print(f"Hello {name}")
        
# Call the function
greet('John', 'Doe', 'Smith')
# Output:
# Hello John
# Hello Doe
# Hello Smith

# So, we can pass any number of arguments to the function using *args.
# and it will be treated as tuple inside the function.

# We can also pass any number of keyword arguments to the function using **kwargs.
# and it will be treated as dictionary inside the function.

# Example:
def greet(**names):
    for key, value in names.items():
        print(f"Hello {key}, {value}")

# Call the function
greet(name1='John', name2='Doe', name3='Smith')
# Output:
# Hello name1, John
# Hello name2, Doe
# Hello name3, Smith

############ Predefined functions ############

# Python has many predefined functions that can be used directly.
# Like we created a function to do a same task everytime, like print a message.
# So, predefined function will also do a specific task everytime when called.
# For example, print(), input(), len(), sum(), max(), min(), upper(), lower(), title(), range(), etc
"""
abs(): Returns the absolute value of a number.
all(): Returns True if all elements of an iterable are true.
any(): Returns True if any element of an iterable is true.
ascii(): Returns a string containing a printable representation of an object.
bin(): Converts an integer to a binary string.
bool(): Converts a value to a Boolean.
bytearray(): Returns a bytearray object.
bytes(): Returns a bytes object.
callable(): Returns True if the object appears callable.
chr(): Returns the character for a given Unicode code point.
classmethod(): Converts a method into a class method.
compile(): Compiles source into a code or AST object.
complex(): Creates a complex number.
delattr(): Deletes an attribute from an object.
dict(): Creates a dictionary.
dir(): Returns a list of the attributes and methods of an object.
divmod(): Returns the quotient and remainder of dividing two numbers.
enumerate(): Returns an enumerate object.
eval(): Evaluates a string as a Python expression.
exec(): Executes a dynamically created program.
filter(): Constructs an iterator from elements of an iterable for which a function returns true.
float(): Converts a value to a floating point number.
format(): Returns a formatted string.
frozenset(): Returns a new frozenset object.
getattr(): Returns the value of a named attribute of an object.
globals(): Returns the current global symbol table as a dictionary.
hasattr(): Returns True if an object has a given attribute.
hash(): Returns the hash value of an object.
help(): Invokes the built-in help system.
hex(): Converts an integer to a hexadecimal string.
id(): Returns the identity of an object.
input(): Reads a line of input from the user.
int(): Converts a value to an integer.
isinstance(): Checks if an object is an instance of a class or of a subclass thereof.
issubclass(): Checks if a class is a subclass of another class.
iter(): Returns an iterator object.
len(): Returns the length of an object.
list(): Creates a list.
locals(): Returns the current local symbol table as a dictionary.
map(): Applies a function to all items in an iterable.
max(): Returns the largest item in an iterable or the largest of two or more arguments.
memoryview(): Returns a memory view object.
min(): Returns the smallest item in an iterable or the smallest of two or more arguments.
next(): Retrieves the next item from an iterator.
object(): Creates a new featureless object.
oct(): Converts an integer to an octal string.
open(): Opens a file and returns a file object.
ord(): Returns the Unicode code point for a single character.
pow(): Returns the value of a number raised to the power of another number.
print(): Prints objects to the text stream file, by default the console.
property(): Returns a property attribute.
range(): Returns a sequence of numbers.
repr(): Returns a string containing a printable representation of an object.
reversed(): Returns a reversed iterator.
round(): Rounds a number to a given precision in decimal digits.
set(): Creates a set.
setattr(): Sets the value of an attribute of an object.
slice(): Returns a slice object.
sorted(): Returns a sorted list from the items in an iterable.
staticmethod(): Converts a method into a static method.
str(): Returns a string object.
sum(): Sums the items of an iterable.
super(): Returns a proxy object that delegates method calls to a parent or sibling class.
tuple(): Creates a tuple.
type(): Returns the type of an object.
vars(): Returns the __dict__ attribute of an object.
zip(): Returns an iterator of tuples.
__import__(): Invokes the import mechanism
__init__(): Constructor (initializer) method called when an object is created.
"""