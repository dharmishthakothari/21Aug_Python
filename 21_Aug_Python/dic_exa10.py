dict1 = {1:0,2:0,3:0, 4:0}
# square only even keys 
dict2 = {k:k**2 for k,v in dict1.items() if k%2==0}
print(dict2)

# convert upper capital whose state's len more then 5 
state_capital={"Gujarat":"Gandhinagar","Rajashthan":"Jaipur","Maharastra":"Mumbai","Orrisha":"Bhuvneshwar"}
state_capital_1 = {k:v.upper() for k,v in state_capital.items() if len(k)>7}

no_dict = {1:"" , 2:"" , 3:"",4:"",5:""}
# no_dict = {1:"ODD" , 2:"EVEN" , 3:"ODD",4:"EVEN",5:"ODD"}

no_dict1 = {k:"EVEN" if k%2==0 else "ODD" for k in no_dict}
print(no_dict1)

# Convert capital into upper if capital is greater then 5 
# else convert capital into lower

state_capital={"Gujarat":"Gandhinagar","Rajashthan":"Jaipur","Maharastra":"Mumbai","Orrisha":"Bhuvneshwar"}
state_capital_1 = {k:v.upper() if len(v)>7 else v.lower() for k,v in state_capital.items()}
print(state_capital_1)