from functools import wraps
import logging
logging.basicConfig(level=logging.INFO)

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling: {func.__name__}")
        logging.info(f"Args: {args}, Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Returned: {result}")
        return result
    return wrapper

@log_decorator
def count(num):
    c=0
    for i in range(1,num):
        c+=1

@log_decorator
def greet(name,msg):
    print(f"{msg}-{name}")


greet(name="Dharmishtha",msg="Have nice Day")
count(20)