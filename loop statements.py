"""n=int(input("Enter a number:"))
temp=0
for i in range(1,n+1,1):
    temp=temp+i
    print(temp)"""
"""n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1,1):
    fact=fact*i
    print(fact)"""
"""n=int(input("Enter a number:"))
temp=0
for i in range(1,n+1,1):
    temp=temp+i*i
    print(temp)"""
"""n=int(input("Enter a number:"))
count=0
if n>1:
    for i in range(2,n):
        if(n%i==0):
            count=1
        break
if count==1:
    print(n,"Is not a prime number")
else:
    print(n,"is a prime number")"""
"""a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print("prime numbers between ",a,b,"are")
for x in range(a,b+1):
    if x>1:
        for i in range(2,x):
            if(x%i==0):
                break
        else:
                print(x)"""
#Fibonacci Series
"""n=int(input("Enter a number:"))
a=0
b=1
print(a)
print(b)
for i in range(0,n,1):
    s=a+b
    a=b
    b=s
    print(s)"""
#Armstrong number
"""n=int(input("Enter a number:"))
temp=n
sum=0
while(temp>0):
    c=temp%10
    sum+=c**3
    temp=temp//10
if(sum==n):
    print(n,"Is a armstrong number")
else:
    print(n,"Is not a armstrong number")"""
#Coprime or not
n1=int(input("Enter a number"))
n2=int(input("Enter a number"))
x=min(n1,n2)
for i in range(1,x+1):
    if n1%i==0 and n2%i==0:
        hcf=i
if hcf==1:
    print(n1,n2,"Are co-prime numbers")
else:
    print(n1,n2,"Are not a co-prime numbers")
                
