import math
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
c=math.gcd(a,b)
if c==1:
    print(a,"and",b,"are coprime")
else:
    print(a,"and",b,"are not a coprime")
    
