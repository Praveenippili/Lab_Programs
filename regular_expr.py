import re
text="vandana age is 18,joshna age is 21"
a=re.search("vandana",text);
b=re.search("good",text);
c=re.findall("age",text);
d=re.findall("me",text);
e=re.split("is",text);
f=re.split("me",text);
g=re.sub("vandana","VANDANA",text);
i=re.sub("joshna","JOSHNA",text);
j=re.sub("21","22",text);
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(i)
print(j)

