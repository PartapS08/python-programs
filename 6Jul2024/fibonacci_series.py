# The program will print the Fibonacci series up to n
print("\033[34mProgram will print the Fibonacci series up to number you gonna enter.\033[0m")
print("\033[36mTere ko pta hai Fibonacci series kya hota hai?")
print("main btata hu, dekho:")
print("Agar aapne 7 daala toh to seriea banegi:")
print("0, 1, 1, 2, 3, 5, 8")
print("matlab pichle do numbers jma krke agla number, total 7 numbers tak.")
print("0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8. total 7 numbers tak, samjha kya?\033[0m")

try:
    num = int(input("\033[33mChal ab tu number daal:\033[0m"))
    if type(num) == int and num < 30:
    #if num.isdigit():
        x = 0
        y = 1 
        z = 0
        print("The series is:")
        for i in range(1, num + 1):
            print(x, end=", ")
            z = x + y
            x = y
            y = z
    elif num > 30:
        print("\033[31myr! tum aakhir karna kya chahta hai?\nItne vehle ni bethe, koi chota number daal.\033[0m")
except:
    print("\033[33mBhai kya kr raha. Number daalne ko bola tha.\033[0m")