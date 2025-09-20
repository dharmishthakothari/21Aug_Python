str = "This is Python class"
print(str[-4])
print(len(str))

name=input("Enter name ")
for i in name:
    print(i)

#accessing thru index
for i in range(len(name)):
    print(f"{i} ---> {name[i]}")
