class Person:
    def __init__(self,name,c_no):
        self.name=name
        self.c_no=c_no
    def display(self):
        print(f"{self.name} - {self.c_no}")        
class Employee(Person):
    def __init__(self, name, c_no,salary):
        super().__init__(name, c_no)        
        self.salary=salary
    def displayEmp(self):
        print(f"{self.name}- {self.c_no} - {self.salary}")

p1=Person("dharmishtha",2345)
p1.display()
emp1=Employee("Abhijit",23456,200000)
emp1.display()
emp1.displayEmp(23)


