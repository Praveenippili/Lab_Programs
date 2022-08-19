Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="vandana"
>>> a
'vandana'
>>> a.index('v');
0
>>> str="i love python"
>>> str.index("love");
2
>>> str.index("0");
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str.index("0");
ValueError: substring not found
>>> str.index('o');
3
>>> str.index(1);
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    str.index(1);
TypeError: must be str, not int
>>> str.index(" ");
1
>>> str.index("o",7,12);
11
>>> a
'vandana'
>>> a.isalnum();
True
>>> x="s180247"
>>> x.isalnum();
True
>>> s="2345678"
>>> s.isalnum();
True
>>> e="##$$"
>>> e.isalnum();
False
>>> a.isalpha();
True
>>> s.isalpha();
False
>>> a.isdecimal();
False
>>> a.isdecimal();
False
>>> q="10,20,30"
>>> q.isdecimal();
False
>>> s"12345"
SyntaxError: invalid syntax
>>> s="12345"
>>> s.isdecimal();
True
>>> a.isdecimal();
False
>>> w="12 34"
>>> w.isdecimal();
False
>>> a.isdigit();
False
>>> s.isdigit();
True
>>> s.isidentifier();
False
>>> a.isidentifier();
True
>>> o="VAndaNA"
>>> o.islower();
False
>>> v="S180247FGHJ"
>>> v.islower();
False
>>> v.isnumeric();
False
>>> s.isnumeric();
True
>>> c="my name is \n vandana"
 a="python is a language"
>>> a.rfind("e");
19
>>> a.rfind("a");
17
>>> a.rfind("g");
18
>>> a.rfind("v");
-1
>>> a.rfind("a",12,19);
17
>>> a.rindex("i");
7
>>> a.rindex("v");
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.rindex("v");
ValueError: substring not found
>>> 
