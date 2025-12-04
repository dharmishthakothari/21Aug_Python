import re
msg="This is beatiful 23456 morning"
match=re.search(r"is ",msg)
#match=re.search(r"\d",msg)
#print(match)

if match:
    print(f"{match.start()} -{match.end()} - {match.span()}")
#match1=re.match(r"\d","23232")
#print(match1)

