#Number is positive or negative
"""n=int(input("Enter a number:"))
if n>0:
    print("Number is positive:",n)
elif n==0:
    print("Number is Zero:",n)
else:
    print("Number is negative:",n)"""
#Number is even or odd
"""n=int(input("Enter a number:"))
if n%2==0:
    print("The number is positive",n)
else:
    print("The number is negetive",n)"""
#Leap year or not
"""year=int(input("Enter the year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,",The given year is leap year")
        else:
            print(year,",The given year is not a leap year")
    else:
        print(year,"The given year is a leapyear")
else:
    print("The given number is not a leap year")"""
x=input("Enter a number:")
y=input("Enter a number:")
z=input("Enter a number:")
if x>y and x>z:
    print("X is a bignumber")
elif y>x and y>z:
    print("Y is bignumber")
else:
    print("Z is a bignumber")

