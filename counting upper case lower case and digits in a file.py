u=0
l=0
d=0
s=0
c=0
f=open("pari.txt","r")
data=f.read()
for x in data:
  if x.islower():
    l+=1
  elif x.isupper():
    u+=1
  elif x.isdigit():
    d+=1
  elif x.isspace():
    s+=1
  else:
    c+=1
print("Upper case letters:",u)
print("Lower case letters:",l)
print("Digits:",d)
print("Spaces:",s)
print("Special characters:",c)
