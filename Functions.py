#Finding lcm
"""n1=int(input("enter a number"))
n2=int(input("enter a number"))
def lcm(x,y):
    if x>y:
        big=x
    else:
        big=y
    while(True):
        if((big%x==0) and (big%y==0)):
            lcm=big
            break
        big=big+1
    return lcm
print("LCM of",n1,n2,"is",lcm(n1,n2))"""
#Finding hcf
"""n1=int(input("Enter a number:"))
n2=int(input("Enter  a number:"))
def hcf(x,y):
    if x>y:
        small=x
    else:
        small=y
    for i in range(1,small+1):
        if((x%i==0) and (y%i==0)):
            gcf=i
    return gcf
print("GCF of ",n1,n2,"is",hcf(n1,n2))"""
#Calculate the no.of upper and lower case letters in a string
"""a=input("Enter a string:")
def str(s):
    d={ "U":0,"L":0}
    for i in s:
        if i.isupper():
            d["U"]+=1
        elif i.islower():
            d ["L"]+=1
        else:
            pass
    print("Original string:",s)
    print("No.of uppercase characters:",d["U"])
    print("No.of lowercase characters:",d["L"])
str(a)"""
#Calculate factorial of a number
"""x=int(input("Enter a nuber:"))
def display(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print("The factorial of ",x,"is",display(x))"""
#CAlculate factorial of a number upto some range
a=int(input("Enter a number:"))
def display(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(display(a))
for i in range(a):
    print(i,displayn(i))

    
