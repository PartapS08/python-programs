for i in range(1,11):
    if i%2==0:
        for x in range(1,i+1):
            print(i,end="")
    elif i==1:
        print(i,end=", ")
    else:
        print(",", i,end=", ")