dict1 = {1:0,2:0,3:0, 4:0}
# for k,v in dict1.items():
#     dict1[k]=k**2

# key - 
# value - 
dict2 = {k:k**2 for k in dict1}
print(dict2)

state_capital={"Gujarat":"Gandhinagar","Rajashthan":"Jaipur","Maharastra":"Mumbai","Orrisha":"Bhuvneshwar"}
# converting cityname in upper case with dict comprehensive
state_capital_upper ={k:v.upper() for k,v in state_capital.items()}
print(state_capital_upper)

state_capital={"Gujarat":7,"Rajashthan":"Jaipur","Maharastra":"Mumbai","Orrisha":"Bhuvneshwar"}
