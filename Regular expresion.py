"""import re
txt="I am vandanadokkara"
x=re.search("^i.*dokkara$",txt)
print(x)"""
"""import re
txt=" I am vandanadokkara"
x=re.search("I am vandanadokkara",txt)
print(x)
x=re.findall("an",txt)
print(x)
x=re.findall("josh",txt)
print(x)
x=re.search("\s",txt)
print("First White space is at",x.start())
x=re.split("\s",txt,1)
print(x)
x=re.sub("\s","@",txt)
print(x)
x=re.sub("\s","@",txt,2)
print(x)
x=re.search("am",txt)
print(x)"""
"""import re
txt=" i am vandana"
x=re.findall("[a-m]",txt)
print(x)"""
"""import re
txt="Vandanaraju 0814"
x=re.findall("[0-7]",txt)
print(x)
txt="Vandana dokkara"
x=re.findall("V.....a",txt)
print(x)
txt="hello worls"
x=re.search("^h",txt)
if x:
    print("matched")
else:
    print("not matched")
x=re.findall("he.+lo",txt)
print(x)"""
import re
txt="vandana dokkara"
x=re.search(r"\bv\w+",txt)
print(x.span())
print(x.string)
print(x.group())

