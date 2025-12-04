def decorator_Parameter(func):
    def wrapper(*args,**krgs):
        print(args)
        print(krgs)
        result=func(*args,**krgs)
        return result
    return wrapper
     

@decorator_Parameter
def greet(name,age,address):
    print(f"Good Morning {name}")

greet("Ishika",20,address="C G Road")
