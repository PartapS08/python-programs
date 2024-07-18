# This program will print series in reverse order.

try:
    num = int(input("Enter the number: "))
    if type(num) == int and num < 99:
    #if num.isdigit():
        print("The series is:")
        for i in range(num,0, -1):
            print(i, end=", ")
    else:
        print("Time lagega bhai, kal aana.")
except:
    print("Invalid input. Please enter a number.")