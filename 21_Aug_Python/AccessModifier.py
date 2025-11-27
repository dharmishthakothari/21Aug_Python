class class1:
    def __init__(self,no1,no2,no3):
        #procted 
        self._no1=no1
        # private data
        self.__no2=no2
        self.no3=no3
    def display(self):
        print(f"{self._no1} - {self.__no2} - {self.no3}")
class class2(class1):
    def display1(self):
        print(self._no1)
        #print(self.__no2)
class class3:
    def greet(self):
        obj=class1(2,3,4)
        print(obj._no1)
obj=class1(12,100,300)
obj.display()
obj1=class2(12,120,456)
obj1.display1()
obj2=class3()
obj2.greet()