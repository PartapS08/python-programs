
class A:
    age=25
    name=input("Enter your name: ")
    place=input("Enter your place: ")
    
    def myfunc(self,name):
        print(name, "is", self.age, "years old")

    def xyfuc(self,place,name):
        print(name ,"is", self.age, "years old and lives in", place)

objA=A()
objA.myfunc(objA.name)
objA.xyfuc(objA.place,objA.name)
