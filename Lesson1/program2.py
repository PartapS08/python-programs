# Display a message based on the marks entered by the user

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >= 50:
    print("Congratulations", name, "you have passed the exam")
else:
    print("Sorry", name, "you have failed the exam")

# Command to run the program:
# python program1.py
# Output:
# Enter your name: John
# Enter your marks: 60
# Congratulations John you have passed the exam