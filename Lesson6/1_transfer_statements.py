# Transfer statements: break, continue, pass, return, raise, assert, yield, import, from, as, global, nonlocal, del, with, async, await.
# These are helpful in controlling the flow of the program.
# They are essential for controlling loops and handling exceptional situations.

# break: It is used to exit a loop when a condition is met.
# continue: It is used to skip the current iteration and continue with the next iteration.
# pass: It is just for doing nothing.

############ break statement ############

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Number to search for
target = 13

# Using break to exit the loop when the target is found
for number in numbers:
    if number == target:
        print(f"Number {target} found in the list.")
        break  # Exit the loop when the target number is found
    print(f"Checked number {number}, not a match.")

# Executed after the loop
print("Search complete.")
# Output:
# Checked number 1, not a match.
# Checked number 3, not a match.
# Checked number 5, not a match.
# Checked number 7, not a match.
# Checked number 9, not a match.
# Checked number 11, not a match.
# Checked number 13, not a match.
# Number 13 found in the list.
# Search complete.

############ continue statement ############

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Number to search for
target = 13

# Using continue to skip the current iteration when the target is found
for number in numbers:
    if number == target:
        print(f"Number {target} found in the list.")
        continue  # Skip the current iteration when the target number is found
    print(f"Checked number {number}, not a match.")

# Executed after the loop
print("Search complete.")
# Output:
# Checked number 1, not a match.
# Checked number 3, not a match.
# Checked number 5, not a match.
# Checked number 7, not a match.
# Checked number 9, not a match.
# Checked number 11, not a match.
# Number 13 found in the list.
# Checked number 15, not a match.
# Checked number 17, not a match.
# Checked number 19, not a match.
# Search complete.


############ pass statement ############

# pass is used when a statement is required syntactically but you do not want any command or code to execute.
# It is used as a placeholder for future code.
# It is used when you do not want to execute any code, but you want to avoid getting an error.

for i in range(5):
    # Placeholder for code implementation
    pass
print("End of loop")

# Output:
# End of loop

def function():
    # Placeholder for function implementation
    pass

# Output:
# No output
