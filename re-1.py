import re
text="Cat,Rat,Mat,Pat"
a=re.findall(r"[A-Z][a-z]",text);
c=re.findall(r"[at]",text);
print(a)
print(c)
