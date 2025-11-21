import traceback
class LengthException(Exception):
    pass
try:
    name=input("Enter name ")
    if len(name)>20:
        raise LengthException("Name must be upto 20 character long")

    address=input("Enter address ")
    if len(address)<5:
        raise LengthException("Address is too short")
    
    age=int(input("Enter age "))
    if age<18:
        raise ValueError("Age must be > 18 ")
except LengthException as e:
    print(f"{e}")
    traceback.print_exc()
except ValueError as e:
    print(f"{e}")
