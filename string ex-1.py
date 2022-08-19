Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="?n vandana"
a.isprintable()
True
a="/n vandana"
a.isprintable()
True
x="my name is /n vandana"
x.isprintable()
True
x="my name is \n vandana"
x.isprintable()
False
a="  "
a.isspace()
True
x.isspace()
False
a="vandana"
a.istitle()
False
x="Vandana"
x.istitle()
True
c="VaNdaANA"
c.istitle()
False
c.isuppar()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    c.isuppar()
AttributeError: 'str' object has no attribute 'isuppar'. Did you mean: 'isupper'?
c.isupper()
False
l=['1','2','3']
r="-"
r.join(l)
'1-2-3'
a
'vandana'
a.rjust(20,"raju")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.rjust(20,"raju")
TypeError: The fill character must be exactly one character long
a.rjust(20,"$")
'$$$$$$$$$$$$$vandana'
a.rjust(20)
'             vandana'
a.ljust(20)
'vandana             '
a.ljust(20,"*")
'vandana*************'
a="vandana is a good and vandana is very beautiful"
a.partition("is")
('vandana ', 'is', ' a good and vandana is very beautiful')
a.replace("vandana","joshna")
'joshna is a good and joshna is very beautiful'
a="kakinadakaja"
a.rfind("a")
11
a.rfind("k")
8
a.rindex("a")
11
a="vandana is a good and vandana is very beautiful"
a.rpartition("is")
('vandana is a good and vandana ', 'is', ' very beautiful')
a="vandana is is is"
a.rpartition("is")
('vandana is is ', 'is', '')
a.rsplit("is")
['vandana ', ' ', ' ', '']
a="vandana is a good and vandana is very beautiful"
a.rsplit("is")
['vandana ', ' a good and vandana ', ' very beautiful']
a="$$$$vandana$$$$$"
a.strip()
'$$$$vandana$$$$$'
a.strip("$")
'vandana'
a="vandana"
a.swapcase()
'VANDANA'
a.capitalize()
'Vandana'
a.title()
'Vandana'
l=["1","2","3","vandana","joshna"]
print(l);
['1', '2', '3', 'vandana', 'joshna']
l[5]="manoj"
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    l[5]="manoj"
IndexError: list assignment index out of range
