class Employee:
    # intilize name 
    def __init__(self,name):
        self.name=name

    #functions 
    def greet(self,name):
        print(f"Good Morning {name} ")
           
dharmishtha=Employee("Dharmishtha ")
dharmishtha.greet()

