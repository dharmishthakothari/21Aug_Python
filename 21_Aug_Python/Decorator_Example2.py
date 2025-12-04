import time
def time_check(func):
    def wrapper():
        print(f"Start At {time.time()}" )
        func()
        print(f"End At {time.time()} " )
    return wrapper
@time_check
def count():
    c=0
    for i in range(100):
        c+=1
count()