# Sequence datatypes are string, list, tuple, range, bytes, bytearray.
# The str type is used to store a sequence of characters (text/words/lines).
# The list type is used to store a sequence of elements using square brackets []. It is mutable.
# The tuple type is used to store a sequence of elements using parentheses (). It is immutable/unchangable.
# The range type is used to store a sequence of numbers.
# The bytes type is used to store a sequence of bytes. It is immutable.
# The bytearray type is used to store a sequence of bytes. It is mutable.
# We have str(), list(), tuple(), range(), bytes(), bytearray() functions in-built in Python. 
# To convert a sequence to a string, list, tuple, range, bytes, and bytearray respectively.

# ########### string example ############

# Remember : input() function always reads the input as a string.
name = input("Enter your name: ")
address = input("Enter your address: ")
city = input("Enter your city: ")
contact = input("Enter your contact number: ")

print("Thank you for providing the details.")
print("Name:", name)
print("Address:", address)
print("City:", city)
print("Contact:", contact)
# Output:
# Enter your name: John
# Enter your address: 4 West 31st Street
# Enter your city: New York
# Enter your contact number: 1234567890

# Thank you for providing the details.
# Name: John
# Address: 4 West 31st Street
# City: New York
# Contact: 1234567890

# In above example all input are stored as string.
# There are many in-built functions to perform operations on string.
# For example, capitalize(), casefold(), center(), count(), encode(), endswith(), expandtabs(), find(), format(), format_map(), 
# index(), isalnum(), isalpha(), isascii(), isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), 
# isspace(), istitle(), isupper(), join(), ljust(), lower(), lstrip(), partition(), replace(), rfind(), rindex(), rjust(), 
# rpartition(), rsplit(), rstrip(), split(), splitlines(), startswith(), strip(), swapcase(), title(), translate(), upper(), 
# zfill() etc.

# ########### list example ############

# List is a collection of items. It is ordered and changeable. Allows duplicate members.
# Ordered means that the items have a defined order, and that order will not change. 
# When we gonna print the list the items will appear in the same order as they were inserted.
# List items are enclosed in square brackets [].
# List can store different data types.
# List is mutable.
# Empty list is defined as var = []. here type(var) will return <class 'list'>.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
married = bool(input("Are you married? True/False: "))
person1 = [name, age, height, married] # saved the inputs in a list

print("Thank you for providing the details.")
print("Name:", person1[0])
print("Age:", person1[1])
print("Height:", person1[2])
print("Married:", person1[3])
# Output:
# Enter your name: John
# Enter your age: 25
# Enter your height: 5.8
# Are you married? True/False: True

# Thank you for providing the details.
# Name: John
# Age: 25
# Height: 5.8
# Married: True

# In the list if you want to change the value of any element you can do it.
# There are many in-built functions to perform operations on list. 
# For example, append(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy(), extend() etc.
# Other operations are Slice operator [:], Membership operators (in, not in), Identity operators (is, is not) etc.
# Each operations we will discuss in example programs files.

# ########### tuple example ############

# Tuple is a collection of items. It is ordered and unchangeable. Allows duplicate members.
# Tuple items are enclosed in parentheses ().
# Tuple can store different data types.
# Tuple is immutable.
# Tuple is faster than list.
# Empty tuple is defined as var = (). here type(var) will return <class 'tuple'>.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
married = bool(input("Are you married? True/False: "))
person2 = (name, age, height, married) # saved the inputs in a tuple

print("Thank you for providing the details.")
print("Name:", person2[0])
print("Age:", person2[1])
print("Height:", person2[2])
print("Married:", person2[3])
# Output:
# Enter your name: John
# Enter your age: 25
# Enter your height: 5.8
# Are you married? True/False: True

# Thank you for providing the details.
# Name: John
# Age: 25
# Height: 5.8
# Married: True

# In the tuple if you want to change the value of any element you can't do it.
# There are few in-built functions to perform operations on tuple. For example, count(), index() etc.
# These operations we will discuss in example programs files.

############ range example #############

# The range() function returns a sequence of numbers.
# starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# In actual it takes 3 arguments range(start, stop, step).
# The range() function only works with the integers.
# Basically the range() function is used to generate a sequence of numbers.
# The range() function is used in for loop. for loop we will discuss in Lesson4.

range = range(5)
print(range)
# Output:
# range(0, 5)

count = range(1, 5)
for i in count:
    print(i)

# Output:
# 1
# 2
# 3
# 4

# There are few in-built functions to perform operations on range. 
# For example: len(), min(), max(), sum(), Membership operators (in, not in), Identity operators (is, is not), Slice operator [:] etc.
# These operations we will discuss in example programs files.
