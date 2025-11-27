from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        return 0.0
class Rectagle(Shape):
    def __init__(self,l,b):
        super().__init__()
        self.b=b
        self.l=l
    def calculateArea(self):
        return self.l*self.b
obj1=Rectagle(2,4)

print(f"Area of Rectagle is {obj1.calculateArea()}")