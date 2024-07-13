'''
class A:
    def __init__(self):
        print("Good Morning")

    def myfunc(self, name):
       print ('Hello', name) 

objA=A()
objA.myfunc("John")
'''

class A:
    def __init__(self, name):
        print("Good Morning", name)
        self.name=name
    def myfunc(self):
       print ('Hello', self.name)

objA=A("John")
objA.myfunc()

