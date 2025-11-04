def checkEven(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
def checkpositive(number):
    if number>0:
        print("Number is Positive")
    else:
        print("Number is Negative ")
def isPrime(number):
    for i in range(2,number):
        if number%i==0:
            return False
    return True
                