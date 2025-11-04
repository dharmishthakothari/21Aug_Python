# import Module1
# Module1.greet("Dhruv")
from Module1 import greet,bye
import CheckNumber

greet("Dhruv")
bye("Abhijit")
print(CheckNumber.checkEven(23))
CheckNumber.checkpositive(23)
if CheckNumber.isPrime(33):
    print("number is Prime")
else:
    print("number is not Prime")