# Program to find the sum of natural numbers up to n

print(f"Enter any number:\n And my program will output the sum of all natural numbers up to that number.")
num = int(input("Enter the number: "))
if type(num) == int:
 #if num.isdigit():
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i
    print(f"The sum of natural numbers up to {num} is: {sum}")
else:
    print("Invalid input. Please enter a number.")


