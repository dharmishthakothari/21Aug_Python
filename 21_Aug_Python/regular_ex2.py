import re
msg="This is beatiful, Today is beatiful Morning"
match=re.search(r"\AMorning",msg)
print(match)

msg1="This is good Morning,good afternoon"
#match=re.search(r"\d+","test 122 123567")
#print(match)

lst=re.findall(r"\d+","test 122 123567")
for i in lst:
    print(i)
lst=re.findall(r"\d+","test 122 123567")

