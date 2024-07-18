num = input("Enter the number:")
length = len(num)
for i in range(length):
    if i <= length - 2:
        print(num[i], end="+")
    else:
        print(num[i])