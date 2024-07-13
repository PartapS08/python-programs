# The input() function is used to take input from the user. It reads the input from the user as a string.
input()
# Output:
# <hello world>

# The input() function always returns a string. If you want to take an integer input, you can use the int() function to convert the string to an integer.
# The input() function can also take a prompt as an argument. The prompt is the message that will be displayed to the user before taking the input.
# following will prompt message "Enter your name: " to the user
input("Enter your name: ")
# Output:
# Enter your name: <John>
# Nothing will be printed on the console as we are just taking the input from the user and not printing it.

print("Hello", input("Enter your name: "))
# Output:
# Enter your name: <John>
# Hello John

# 2nd method is to take input from user and save in a variable.
name = input("Enter your name: ")
print("Hello", name, "!")
# Output:
# Enter your name: <John>
# Hello John !

# The input() function always returns a STRING. If you want to take an integer input, you can use the int() function to convert the string to an integer.
(input("Enter your age: "))
# Output:
# Enter your age: <25>
# 25 is a string here and we cant perform any arithmetic operation on it (sum, subtraction, multiplication, division etc)
int(input("Enter your age: "))
# Output:
# Enter your age: <25>
# 25 is a integer here and we can perform any arithmetic operation on it (sum, subtraction, multiplication, division etc)

# 2nd method is to take input from user and save in a variable.
age =  int(input("Enter your age: "))
print("You are", age, "years old")
year_of_birth = 2024 - age
print(F"You were born in {year_of_birth}.")
# Output:
# Enter your age: <25>
# You are 25 years old
# You were born in 1999.
