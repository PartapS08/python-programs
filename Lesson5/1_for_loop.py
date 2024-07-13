# For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# For loop is used where we know the number of iterations, 
# but we will use while loop where we do not know the number of iterations in advance.
# For loop is used to execute a block of code multiple times.

############ for loop ############

# Print even numbers from 0 to 10
for i in range(0, 10):
    if i % 2 == 0:
        print(i)

# Output:
# 0
# 2
# 4
# 6
# 8


# Print odd numbers from 0 to 10
for i in range(1, 10, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9


############ for loop with list ############

# Print elements of a list
fruits = ['apple', 'banana', 'cherry', 'mango', 'orange']
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
# mango
# orange


