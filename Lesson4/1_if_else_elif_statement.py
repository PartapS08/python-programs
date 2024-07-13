# Conditional statements are if, elif, else.
# Just if statement is used to check a condition and execute code if the condition is true.
# if and else statement is used to check a condition and execute code if the condition 
# is true and execute another code if the condition is false.
# Finally, if, elif, else statement is used to check multiple conditions, where outputs 
# could be 3 or more.

############ if statement ############

Score = 80
if Score > 50:
    print('You passed the exam')

# Output:
# You passed the exam


############ if else statement ############

Score = 40
if Score > 50:
    print('You passed the exam')
else:
    print('You failed the exam')

# Output:
# You failed the exam


############ if elif else statement ############

Score = 40
if Score >= 80:
    print('You passed the exam')
elif Score > 60 and Score < 80:
    print('You got to reappear')
else:
    print('You failed the exam')

# Output:
# You failed the exam


