import traceback
try:
    no=int(input("Enter number"))
    print(f"Here is no {no}")
except:
    traceback.print_exc()
else:
    print("In Else ")
finally:
    print("in Finally ")
