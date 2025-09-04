age = int(input("Enter age "))
if age>=0 and age<=2:
    print("Infant")
elif age>=3 and age<18:
    print("minor")
elif age>=18 and age<=50:
    print("Adult")
elif age>50:
    print("Senior")
else:
    print("Invalid age")
