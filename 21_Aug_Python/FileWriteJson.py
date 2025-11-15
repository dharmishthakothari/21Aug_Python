import json
data={'age':22,'address':'CG Road'}
with open('File1.json',"w") as file:
    json.dump(data,file)
    print("Data Written Successfully ")