file = open("C:\\Users\\Admin\\Downloads\\SQL_Query.txt","r")
#file = open("NewFile.txt.txt","r")
while True:
    data=file.readline()
    print(data)
    if not data :
        break
# -1 EOF