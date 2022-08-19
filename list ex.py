Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[1,2,3,4,"vandana","joshna","manoj"]
a.append("kamala","apparao")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a.append("kamala","apparao")
TypeError: list.append() takes exactly one argument (2 given)
a.append("kamala")
print(a)
[1, 2, 3, 4, 'vandana', 'joshna', 'manoj', 'kamala']
a.insert(3,"apparao")
a
[1, 2, 3, 'apparao', 4, 'vandana', 'joshna', 'manoj', 'kamala']
x="vand"
x1="nbva"
x.extend(x1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x.extend(x1)
AttributeError: 'str' object has no attribute 'extend'
x=["vandana"]
x1=["joshna"]
x.extend(x1)
print(x)
['vandana', 'joshna']
x1.extend(x)
x1
['joshna', 'vandana', 'joshna']
l=[1,2,3,4,5]
sum(l)
15
l.count("2")
0
x=["vandana"]
x.count("a")
0
len(x)
1
x=["vandana","joshna","manoj"]
len(x)
3
l=["1","2","3","4","5","6"]
l.index("2")
1
l=["1","2","3","4","5","6","2"]
l.count("2")
2
min(l)
'1'
max(l)
'6'
l.reverse()
l
['2', '6', '5', '4', '3', '2', '1']
l.sort(reverse==True)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l.sort(reverse==True)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
l.sort()
l
['1', '2', '2', '3', '4', '5', '6']
pop("2")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    pop("2")
NameError: name 'pop' is not defined. Did you mean: 'pow'?
l.pop("2")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    l.pop("2")
TypeError: 'str' object cannot be interpreted as an integer
l.pop(2)
'2'
l
['1', '2', '3', '4', '5', '6']
l.remove("6")
l
['1', '2', '3', '4', '5']
del(l.append[1])
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    del(l.append[1])
TypeError: 'builtin_function_or_method' object does not support item deletion
del(l.1)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
del(l,[1])
SyntaxError: cannot delete literal
l.clear()
l
[]
