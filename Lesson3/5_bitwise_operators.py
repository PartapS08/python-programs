# Bitwise operators are & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), and >> (right shift).
# Bitwise operators work on bits and perform bit-by-bit operations.


############ Bitwise AND operator ############

a = 10
b = 4
print("a & b =", a & b)
# Output:
# a & b = 0
# Expalanation: 
# 10 in binary is 1010 and 
# 4 in binary is 0100.
# assuming 0 as False and 1 as True, if we apply AND operation 
# on 1010 and 0100, we get 0000 which is 0 in decimal. So output is 0.


############ Bitwise OR operator ############

a = 10
b = 4
print("a | b =", a | b)
# Output:
# a | b = 14
# Expalanation:
# 10 in binary is 1010 and
# 4 in binary is 0100.
# Applying OR operation on 1010 and 0100. 
# we get 1110 which is 14 in decimal. So output is 14.


############ Bitwise XOR operator ############

a = 10
b = 4
print("a ^ b =", a ^ b)
# Output:
# a ^ b = 14
# Expalanation:
# 10 in binary is 1010 and
# 4 in binary is 0100.
# Applying XOR operation on 1010 and 0100.
# we get 1110 which is 14 in decimal. So output is 14.


############ Bitwise NOT operator ############

a = 10
print("~a =", ~a)
# Output:
# ~a = -11
# Expalanation:
# 10 in binary is 1010.
# Applying NOT operation on 1010.
# we get 0101 which is -11 in decimal. So output is -11.


############ Bitwise left shift operator ############

a = 10
print("a << 1 =", a << 1)
# Output:
# a << 1 = 20
# Expalanation:
# 10 in binary is 1010.
# Applying left shift operation on 1010.
# we get 10100 which is 20 in decimal. So output is 20.


############ Bitwise right shift operator ############

a = 10
print("a >> 1 =", a >> 1)
# Output:
# a >> 1 = 5
# Expalanation:
# 10 in binary is 1010.
# Applying right shift operation on 1010.
# we get 101 which is 5 in decimal. So output is 5.
# In right shift, the rightmost bit is removed and leftmost bit is filled with 0.

