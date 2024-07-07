# Author: Gurpartap Singh
# print(): built-in Python function that outputs data to the console
# "Hello World !!": string data that is passed to the print() function

print("Hello World !!")

# Output: 
# Hello World !!

# It can take one or more arguments and will print each of them, separated by spaces, followed by a newline character.
# Double quotes (") are used to define the start and end of a STRING* in Python. You can also use single quotes (') to define strings
# String is a datatype in Python. we will cover it in detail in lesson2.
# Here, variable named "name" is assigned the string value "John". we call is Variable Assignment
# where = is a assignment operator, we will cover it in operators section in lesson3.

name = "John"
print("Hello",name, "How are you?")
print("Welcome to Python Programming")

# Output: 
# Hello John  How are you?
# Welcome to Python Programming

# You can also use f-string to format the string
# {name} is a placeholder that will be replaced by the value of the name variable.
# f-string is a string that is prefixed with 'f' or 'F'. It is used to embed expressions inside string literals, using curly braces {}.

print(f"Hello {name}, How are you?")

# Output:
# Hello John, How are you?