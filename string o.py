{Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="vandana"
>>> a.casefold(();
	   
SyntaxError: invalid syntax
>>> a.casefold();
'vandana'
>>> a.center(30,"#");
'###########vandana############'
>>> a.center(24);
'        vandana         '
>>> a.count("a");
3
>>> a.count("an");
2
>>> a.count("an",'a'=2,'n'=7);
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> a.encode();
b'vandana'
>>> a.endswith("na",1,7);
True
>>> a.endswith("va");
False
>>> a.endswith("na",7,1);
False
>>> expandtabs(20);
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    expandtabs(20);
NameError: name 'expandtabs' is not defined
>>> a.expandtabs(20);
'vandana'
>>> a.expandtabs();
'vandana'
>>> print(a.expandtabs());
vandana
>>> x="i am a good girl";
>>> x.expantabs();
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x.expantabs();
AttributeError: 'str' object has no attribute 'expantabs'
>>> x.expandtabs();
'i am a good girl'
>>> x.expandtabs(20);
'i am a good girl'
>>> print(x.x.expandtabs());
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(x.x.expandtabs());
AttributeError: 'str' object has no attribute 'x'
>>> print(x.expandtabs());
i am a good girl
>>> print(x.expandtabs(2));
i am a good girl
>>> print(x.expandtabs(20));
i am a good girl
>>> print(x.expandtabs())
i am a good girl
>>> a.find("nda");
2
>>> a.find("a",0,4);
1
>>> a.find("a",0,7);
1
>>> a.find("n",0,7);
2
>>> a.find("r",0,7);
-1
>>> 
               
