from abc import ABC, abstractmethod

class Bank(ABC):
    def database(self):
        print("Database is connected")
    @abstractmethod
    def getROI(self):
        pass
    @abstractmethod
    def getROR(self):
        pass

class SBI(Bank):
    def system(self):
        print("Welcome to SBI Bank")
    def getROI(self):
        print("SBI Rate of Interest is 8%")
    def getROR(self):
        print("SBI Rate of Return is 10%")


class HDFC(Bank):
    def getROI(self):
        print("HDFC Rate of Interest is 9%")


obj=SBI()
obj.system()
obj.getROR()

