x=int(input("enter a number:"))
a=0
b=1
print("fibonaccis",a,b)
for i in range(2,x):
    c=a+b
    a=b
    b=c
print(c);
