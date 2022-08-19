Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="vandana";
>>> a.capitalize();
'Vandana'
>>> a.casefold();
'vandana'
>>> a.count();
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.count();
TypeError: count() takes at least 1 argument (0 given)
>>> count(a);
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    count(a);
NameError: name 'count' is not defined
>>> a.count(a);
1
>>> a.encode();
b'vandana'
>>> a.count('a');
3
>>> a.endswith('a');
True
>>> a.endswith('d');
False
>>> a.expandtabs();
'vandana'
>>> a.find('d');
3
>>> a.find('n');
2
>>> a.format();
'vandana'
>>> format(a);
'vandana'
>>> a.format_map();
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.format_map();
TypeError: str.format_map() takes exactly one argument (0 given)
>>> a.index('v');
0
>>> a.index(-1);
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.index(-1);
TypeError: must be str, not int
>>> a.isalnum();
True
>>> a.isalpha();
True
>>> a.isascii();
True
>>> x="234vand";
>>> x.isalnum();
True
>>> x.isalpha();
False
>>> x.isascii();
True
>>> a.isdigit();
False
>>> x.isdigit();
False
>>> a.isidentifier();
True
>>> x.isidentifier();
False
>>> a.islower();
True
>>> c="vM";
>>> c.islower();
False
>>> a.isnumaric();
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.isnumaric();
AttributeError: 'str' object has no attribute 'isnumaric'
>>> a.isnumeric();
False
>>> x.isnumeric();
False
>>> s="1234567";
>>> s.isnumeric();
True
>>> a.isprintable();
True
>>> s.isprintable();
True
>>> r="    @";
>>> r.isprintable();
True
>>> e="   ";
>>> e.isprintable();
True
>>> r.isspace();
False
>>> e.isspace();
True
>>> x.istitle();
False
>>> a.istitle();
False
>>> e.istitle();
False
>>> r.istitle();
False
>>> a.isupper();
False
>>> a.join();
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.join();
TypeError: str.join() takes exactly one argument (0 given)
>>> x.join('a');
'a'
>>> x
'234vand'
>>> a.title();
'Vandana'
>>> a.istitle();
False
>>> w="SD";
>>> w.istitle();
False
>>> a.zfill('2');
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.zfill('2');
TypeError: 'str' object cannot be interpreted as an integer
>>> a.zfill();
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.zfill();
TypeError: str.zfill() takes exactly one argument (0 given)
>>> zfill(a);
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    zfill(a);
NameError: name 'zfill' is not defined
>>> a.zfill('a');
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.zfill('a');
TypeError: 'str' object cannot be interpreted as an integer
>>> x.zfill('v');
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    x.zfill('v');
TypeError: 'str' object cannot be interpreted as an integer
>>> x.zfill(2);
'234vand'
>>> a.translate();
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.translate();
TypeError: str.translate() takes exactly one argument (0 given)
>>> a.strip();
'vandana'
>>> q="qugdydgq";
>>> q.strip();
'qugdydgq'
>>> a.startswith("v");
True
>>> a.startswith("w");
False
>>> a.rpartition();
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.rpartition();
TypeError: str.rpartition() takes exactly one argument (0 given)
>>> a.rpartition("a");
('vandan', 'a', '')
>>> a.partition("n");
('va', 'n', 'dana')
>>> a.rsplit('v');
['', 'andana']
>>> a.rsplit("a");
['v', 'nd', 'n', '']
>>> a.rstrip();
'vandana'
>>> r.rstrip();
'    @'
>>> x.replace('2','3');
'334vand'
>>> 