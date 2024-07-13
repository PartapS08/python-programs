class B:
    name="John"
    print(name)

objB=B()
print(objB.name)
objB.name="Sam"

class A:
    age=25
    print(age)
    def myfunc(self):
        print("Good Morning")
    
objA=A()
objA.myfunc()
