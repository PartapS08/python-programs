# List of Arithmetic Operators are as follows:
# '+', '-', '*', '/', '//', '%', '**'

# Addition
print(10 + 5)
# Output:
# 15

# Subtraction
print(10 - 5)
# Output:
# 5

# Multiplication
print(10 * 5)
# Output:
# 50

# Division
print(10 / 5)
# Output:
# 2.0

# Floor Division gives the integer part of the division.
# Floor Division
print(10 // 5)
# Output:
# 2

# Modulus gives the remainder part of the division.
# Modulus
print(10 % 5)
# Output:
# 0

# Exponent
print(10 ** 5)
# Output:
# 100000

####### Addition Example ########

# Addition of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print("Sum is =", result)
# Output:
# Enter first number: 10
# Enter second number: 20
# Sum is = 30

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = num1 + num2
print("Sum is =", result)
# Output:
# Enter first number: 10
# Enter second number: 20
# Sum is = 1020
# Here the output is 1020 instead of 30 because the input function returns a string value.
# Similary, is first number is John and second number is Wick, then the output will be JohnWick (not John Wick)

####### Subtraction Example ########

# Subtraction of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 - num2
print("Difference is =", result)
# Output:
# Enter first number: 20
# Enter second number: 10
# Difference is = 10

# Subtraction do not work with strings

####### Multiplication Example ########

# Multiplication of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 * num2
print("Product is =", result)
# Output:
# Enter first number: 10
# Enter second number: 20
# Product is = 200

# Multiplication do not work with strings

####### Division Example ########

# Division of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 / num2
print("Quotient is =", result)
# Output:
# Enter first number: 20
# Enter second number: 10
# Quotient is = 2.0

# Division always returns a float value.
# Division do not work with strings
# In case of infinite division, it will throw Error.

####### Floor Division Example ########

# Floor Division of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 // num2
print("Quotient is =", result)
# Output:
# Enter first number: 20
# Enter second number: 10
# Quotient is = 2

# Floor Division always returns an integer value.
# Floor Division do not work with strings
# In case of infinite division, it will throw Error.

####### Modulus Example ########

# Modulus of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 % num2
print("Remainder is =", result)
# Output:
# Enter first number: 20
# Enter second number: 10
# Remainder is = 0

# Modulus always returns an integer value.
# Modulus do not work with strings
# In case of infinite division, it will throw Error.

####### Exponent Example ########

# Exponent of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 ** num2
print("Result is =", result)
# Output:
# Enter first number: 2
# Enter second number: 3
# Result is = 8

# Exponent always returns an integer value.
# Exponent do not work with strings
# In case of infinite division, it will throw Error.
# Exponent do not work with negative numbers.
