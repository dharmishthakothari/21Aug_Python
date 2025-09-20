msg="Have a good day!!!"
print(msg.endswith("test"))
email = input("Enter email id ")
ans=email.endswith(".com")
#if email.endswith(".com"):
if ans:    
    print(f"{email} is valid email address")
else:
    print(f"{email} is invalid email address")

