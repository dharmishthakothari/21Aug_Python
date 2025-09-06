age = int(input("Enter age "))
weight = int(input("Enter weight"))
if age>18:
    if weight>55:
        print("Eligible to donate blood")
    else:
        print("Not eligible to donate blood due to underweight")
else:
    print("Not eligible to donate blood due to age")

# if age>18 and weight>55:
#     print("Eligible to donate blood")
# else:
#     print("Not eligible to donate blood")