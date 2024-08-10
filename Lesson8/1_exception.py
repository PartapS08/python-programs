# If we have some exceptions in our logic or loop, then the program will throw an error and stop the execution.
# But we can handle the exception using try-except block.

# Example: Divide two numbers
a = 10
b = 0
print(a/b)
# Output:
#    print(a/b)
#          ~^~
# ZeroDivisionError: division by zero
# You will see the error message like above.

# Now, let's handle the exception using try-except block.
try:
    a = 10
    b = 0
    print(a/b)
except:
    print("Division by zero is not allowed.")
# Output:
# Division by zero is not allowed.

