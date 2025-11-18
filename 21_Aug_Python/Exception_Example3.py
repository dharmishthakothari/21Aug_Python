try:
    no = input("Enter number ")
    no1=int(no)
    print(f"Value is {no1}")

    ans=no1/2

    print(f"Ans {ans}")
except ZeroDivisionError:
    print("There is an ZeroDivisionError ")  
except ValueError:
    print("There is ValueError")
finally:
    print("Have a greate day!!!")