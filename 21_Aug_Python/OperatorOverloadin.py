class Distance:
    
    def __init__(self,feet,inch):
        self.feet=feet
        self.inch=inch
    def __add__(self,obj2):
        #d1.add(d2)
        #d3=d1.add(d2)
        inch1=self.inch+obj2.inch
        feet1=self.feet+obj2.feet

        obj=Distance(feet1,inch1)
        return obj
    def display(self):
        print(f"{self.feet} - {self.inch}")

    def __lt__(self,other):
        if self.feet<other.feet and self.inch<other.inch:
            return True
        else:
            return False
d1=Distance(12,2)
d2=Distance(15,10)
d1.display()
d2.display()
d3=Distance(0,0)
d3=d1+d2
d3.display()
ans=d1<d2
print(ans)