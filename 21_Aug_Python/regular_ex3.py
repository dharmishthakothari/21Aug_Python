import re
msg="This is IND, This is JPA"
match=re.search(r"JPA$",msg)
print(match)