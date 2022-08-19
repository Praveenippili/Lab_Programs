import re
text="Vandana age is 18,Joshna age is 21,Manoj age is 16,Kamala age is 45"
a=re.findall(r"[A-Z][a-z]+",text);
b=re.findall(r"[0-9]{2}",text);
c={}
i=0;
for name in a:
    c[name]=b[i]
    i=i+1
print(a)
print(b)
print(c)
