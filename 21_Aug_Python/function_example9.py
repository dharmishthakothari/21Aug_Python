def personDetails(**kwargs):
    #print(kwargs)
    if kwargs['age']>=30:
        print(kwargs['name'])
def details():
    return 1,"Dharmishtha",30,"Python"
personDetails(name="Dharmishtha",age=30)
personDetails(city="Ahedmbad",name="Dhruv",age=20)
personDetails(name="Abhijit",age=22)
personDetails(name="etets",age=30)
print(details())