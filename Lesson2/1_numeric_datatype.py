# Numeric data types are int, float, and complex. 
# The int datatype is used to store integer values or in simple words store numbers.
# The float datatype is used to store floating-point numbers or in simple words store decimal numbers.
# The complex datatype is used to store complex numbers eg. 3 + 5j where j is the imaginary part.
# We have int(), float(), and complex() functions in-built in Python 
# to convert a number to an integer, float, and complex number respectively.

########### integer example ############

# Calcuate the area of a square.
side = input("Enter the side of the square: ")
a = int(side)
area = a * a
print("The area of the square is", area, "sq units")
# Output:
# Enter the side of the square: 5
# The area of the square is 25 sq units

############ float example #############

# Calculate the area of a circle.
radius = input("Enter the radius of the circle: ")
r = float(radius)
area = 3.14 * r * r
print("The area of the circle is", area)
# Output:
# Enter the radius of the circle: 5
# The area of the circle is 78.5

############ complex example #############

# Complex numbers are written with a "j" as the imaginary part.
# j or J is standard notation for the imaginary unit. You can't replace it with any other letters.
# Complex numbers are not used much in Python programming.
# But you can use the complex() function to create a complex number.
# The complex number has a real part and an imaginary part.
# The real part is 3 and the imaginary part is 5.
x = complex(3, 5)
print(x)
# Output:
# (3+5j)

# You can also use the complex() function to convert a number to a complex number.
# The real part is 3 and the imaginary part is 0.
x = complex(3)
print(x)
# Output:
# (3+0j)

# Function to perform arithmetic operations on complex numbers.
x = complex(input("Enter the first complex number: "))
y = complex(input("Enter the second complex number: "))
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
# Output:
# Enter the first complex number: 3+5j
# Enter the second complex number: 2+3j
# Addition: (5+8j)
# Subtraction: (1+2j)
# Multiplication: (-9+19j)
# Division: (1.6153846153846154+0.07692307692307693j)
