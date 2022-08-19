##calculate n^th term in fabonaccis series:
x=int(input("enter a number:"))
a=0
b=1
for i in range(2,x):
    c=a+b
    a=b
    b=c
print(c)

##calculate less then the number:
x=int(input("enter a number:"))
a=0
b=1
print("fibonaccis series is:",a,b);
for i in range(2,x):
    c=a+b
    a=b
    b=c
    if(c<x):
        print(c)
