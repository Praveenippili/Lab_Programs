Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5,6,7]
>>> print(l);
[1, 2, 3, 4, 5, 6, 7]
>>> print(l(0));
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(l(0));
TypeError: 'list' object is not callable
>>> print(l[0]);
1
>>> print(l[-1]);
7
>>> l[1]=20;
>>> l
[1, 20, 3, 4, 5, 6, 7]
>>> print(l[5:]);
[6, 7]
>>> i.extend([8,9,10])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    i.extend([8,9,10])
NameError: name 'i' is not defined
>>> l.extend([8,9,10])
>>> l
[1, 20, 3, 4, 5, 6, 7, 8, 9, 10]
>>> len(l);
10
>>> l.append(11);
>>> l
[1, 20, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> len(l);
11
>>> l.append(12,13,14)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l.append(12,13,14)
TypeError: list.append() takes exactly one argument (3 given)
>>> l.append([12,13,14])
>>> len(l)
12
>>> l
[1, 20, 3, 4, 5, 6, 7, 8, 9, 10, 11, [12, 13, 14]]
>>> l.insert(1,000);
>>> l
[1, 0, 20, 3, 4, 5, 6, 7, 8, 9, 10, 11, [12, 13, 14]]
>>> l.insert(1,090);
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> l.insert(1,988);
>>> l
[1, 988, 0, 20, 3, 4, 5, 6, 7, 8, 9, 10, 11, [12, 13, 14]]
>>> l.remove(10);
>>> l
[1, 988, 0, 20, 3, 4, 5, 6, 7, 8, 9, 11, [12, 13, 14]]
>>> l.remove(1);
>>> l
[988, 0, 20, 3, 4, 5, 6, 7, 8, 9, 11, [12, 13, 14]]
>>> del(l[0])
>>> print(l);
[0, 20, 3, 4, 5, 6, 7, 8, 9, 11, [12, 13, 14]]
>>> l[1:3]=[100,200,300]
>>> print(l);
[0, 100, 200, 300, 4, 5, 6, 7, 8, 9, 11, [12, 13, 14]]
>>> l.sort();
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    l.sort();
TypeError: '<' not supported between instances of 'list' and 'int'
>>> del(l[11]);
>>> del(l[12]);
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    del(l[12]);
IndexError: list assignment index out of range
>>> l
[0, 4, 5, 6, 7, 8, 9, 11, 100, 200, 300]
>>> l.sort();
>>> l
[0, 4, 5, 6, 7, 8, 9, 11, 100, 200, 300]
>>> l.sort(reverse=True)
>>> print(l)
[300, 200, 100, 11, 9, 8, 7, 6, 5, 4, 0]
>>> l.sort(reverse)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l.sort(reverse)
NameError: name 'reverse' is not defined
>>> l.sort(reverse=False)
>>> print(l);
[0, 4, 5, 6, 7, 8, 9, 11, 100, 200, 300]
>>> l.reverse()
>>> print(l);
[300, 200, 100, 11, 9, 8, 7, 6, 5, 4, 0]
>>> l=[1,2,3]
>>> m=l
>>> print(l);
[1, 2, 3]
>>> print(m);
[1, 2, 3]
>>> l.extend(4);
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    l.extend(4);
TypeError: 'int' object is not iterable
>>> l.extend([4]);
>>> print(l);
[1, 2, 3, 4]
>>> print(m);
[1, 2, 3, 4]
>>> n=m.copy();
>>> print(n);
[1, 2, 3, 4]
>>> n.extend([9])
>>> print(n);
[1, 2, 3, 4, 9]
>>> print(m);
[1, 2, 3, 4]
>>> print(l);
[1, 2, 3, 4]
>>> 