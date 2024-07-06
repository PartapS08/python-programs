import os

a = int(input('Enter numeric value for a : '))
b = int(input('Enter numeric value for b : '))
print(type(a), type(b))
#exit()

try:
    with open('a.txt', 'w') as afile:
        afile.write(str(a))
    with open('b.txt', 'w') as bfile:
        bfile.write(str(b))
    with open('c.txt', 'w') as cfile:
        cfile.write(str(a+b))
except:
    print('Error in writing files')
