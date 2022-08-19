##using if:
a=int(input("enter a number:"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if(a>b and a>c):
    print("a is big")
if(b>c and b>a):
    print("b is big")
if(c>a and c>b):
    print("c is big")


##using if-else:
a=int(input("enter a number:"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if(a>b and a>c):
    print("a is big")
if(b>a and b>c):
    print("b is big")
else:
    print("c is big")

##using nested-if:
a=int(input("enter a number:"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a>b:
 if a>c:
    print("a is big")
 else:
    print("c is big")
else:
    if b>c:
        print("b is big")
    else:
        print("c is big")

##elif:
a=int(input("enter a number:"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if(a>b and a>c):
    print("a is big")
elif(b>c):
    print("b is big")
else:
    print("c is big")

    
        
    
    

