from abc import ABC,abstractmethod
class class1(ABC):
    @abstractmethod
    def greet(self):
        pass
    def greet1(self):
        print("Good Morning")
class class2(class1):
    pass
    # def greet(self):
    #     print("Have a nce day ")
#obj=class1()
obj1=class2()
obj1.greet()
obj1.greet1()