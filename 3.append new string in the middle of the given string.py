n=input("Enter a string:")
a=input("Enter string to be inserted:")
l=int(len(n)/2)
x=n[:l+1]
x=x+a
x=x+n[l:]
print(x)
