# Program to find the factorial of up to n

print("Program will find the factorial of a number.")
print(f"For Example: factorial of 4 is 24\n 4*3*2*1 = 24.")
try:
    num = int(input("Enter the number: "))
    if type(num) == int and num < 15:
    #if num.isdigit():
        facto = 1
        for i in range(1, num + 1):
            facto = facto*i
        print(f"The factorial answer for {num} is: {facto}")
    else:
        print("Choti value daal bhai. 15 se choti rakh")
except:
    print("Invalid input. Please enter a number.")
