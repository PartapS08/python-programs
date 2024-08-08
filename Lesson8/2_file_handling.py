# How to deal with files and directories in Python
# First we need to import the os module in Python. 'import os'
# then only we can use functions like open(), read(), write(), close(), remove(), mkdir(), rmdir(), etc. in our program.
# The os module provides a way to interact with the operating system.

############# Create a Empty file #############

import os

x=open('file.txt', 'w')
x.close()

# The above code will create a file named file.txt in the current directory.

############# Write to a file #############

import os

x=open('file.txt', 'w')
x.write('Hello, welcome to Python programming')
x.close()

# The above code will write the text 'Hello, welcome to Python programming' to the file file.txt.

############# Read from a file #############

import os

x=open('file.txt', 'r')
print(x.read())
x.close()

# The above code will read the text from the file file.txt and print it on the console.

############# Append to a file #############

import os

x=open('file.txt', 'a')
x.write('This is session on file handling')
x.close()

# The above code will append the text 'This is session on file handling' to the file file.txt.

############# Delete a file #############

import os

os.remove('file.txt')

# The above code will delete the file file.txt.


############# Create a directory #############

import os

os.mkdir('NewFolder')

# The above code will create a directory named NewFolder in the current directory.

############# Delete a directory #############

import os

os.rmdir('NewFolder')

# The above code will delete the directory NewFolder.


############# Check if a file exists #############

import os

if os.path.exists('file.txt'):
    print('File exists')
else:
    print('File does not exist')
    
# The above code will check if the file file.txt exists in the current directory or not.
# Same way we can check if a directory exists or not.

############# Get the current working directory #############

import os

print(os.getcwd())

# The above code will print the current working directory absolute path.

############# Change the current working directory #############

import os

os.chdir('C:/Users/John/Desktop')

# The above code will change the current working directory to C:/Users/John/Desktop.

############# List files and directories in a directory #############

import os

print(os.listdir())

# The above code will list all the files and directories in the current working directory as a list.

############# Rename a file or directory #############

import os

os.rename('file.txt', 'newfile.txt')

# The above code will rename the file file.txt to newfile.txt.

############# Get the file size #############

import os

print(os.path.getsize('newfile.txt'))

# The above code will print the size of the file newfile.txt in bytes.
# to convert it to KB, MB, GB, etc. divide it by 1024, 1024*1024, 1024*1024*1024, etc.
print(os.path.getsize('newfile.txt')/1024)

############# Get the file creation time #############

import os
import datetime

print(os.path.getctime('newfile.txt'))

# The above code will print the creation time of the file newfile.txt in seconds since epoch.
# To convert it to a readable format, use the datetime module.
print(datetime.datetime.fromtimestamp(os.path.getctime('newfile.txt')))
# We have creation time, modification time, and access time of a file. getctime(), getmtime(), getatime() functions respectively.

############# Copy a file #############

import os

with open('newfile.txt', 'r') as f:
    with open('newfile_copy.txt', 'w') as j:
        for line in f:
            j.write(line)
            
# The above code will copy the contents of the file newfile.txt to newfile_copy.txt.
# If destination file does not exist, it will be created. If it exists, it will be overwritten.

# Another way to copy a file is using shutil module.

import shutil

shutil.copy('newfile.txt', 'newfile_copy.txt')

# The above code will copy the file newfile.txt to newfile_copy.txt.


############# Move a file #############

import os

os.rename('newfile.txt', 'C:/Users/John/Desktop/newfile.txt')

# The above code will move the file newfile.txt to the Desktop directory.

############# Check if a path is a file or directory #############

import os

print(os.path.isfile('newfile.txt'))
print(os.path.isdir('newfile.txt'))

# Result will be True or False.

############# Check if a path is absolute or relative #############

import os

print(os.path.isabs('newfile.txt'))

# Result will be True or False.

############# Generate random bytes #############

import os

#Usage : os.urandom(size) 
print(os.urandom(10))
# Output: b'\xc2\xf5\xf7\xc1&0\x03wR<'
# generate only alphanumeric characters
print(os.urandom(10).hex())
# Output: 'c2f5f7c126300377523c'

##################################################

# There are many more functions in the os module that i will not cover here.
# Those are related to file permissions, file attributes, metadata, symlink and hard link etc.
# Others are related to environment variables, system information, etc.
# You can refer to the official documentation for more information.