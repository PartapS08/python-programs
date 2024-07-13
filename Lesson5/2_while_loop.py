# While loop is used to execute a block of code repeatedly as long as the condition is true.
# While loop is used where we do not know the number of iterations in advance.

############ while loop ############

password = 'hello123'
a = input('Enter the password: ')
while a != 'password':
    print('Incorrect password')
    a = input('Enter the password again: ')
print('Logged in successfully')

# Output:
# Enter the password: <password123>
# Incorrect password
# Enter the password again: <abc123>
# Incorrect password
# Enter the password again: <monday123>
# Incorrect password
# Enter the password again: <hello123>
# Logged in successfully

# In the above example, the user is asked to enter the password. 
# If entered password is incorrect, it will not come out of the loop. 
# It will keep running same code inside while loop until the correct password is entered.
# Here we don't know how many times the user will enter the wrong password.