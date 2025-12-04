def decorate(func):
    def wrapper():
        print("Function Calling ")
        func()
        print("Function Ending")
    return wrapper
@decorate
def greet():
    print("Good Morning")

@decorate
def addition():
    print(12+23)
greet()
addition()