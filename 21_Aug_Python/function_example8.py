def addition(*args):
    sum=0
    for i in args:
        if type(i)==int:
            sum+=i
    return sum
ans=addition(12,23)
print(ans)
print(addition(23,657,5656))
print(addition(23,345,567567,13123,34.5656))
print(addition(23,345,"ertertre",567567,13123))
