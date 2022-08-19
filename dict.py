Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={1:"vandana",2:"joshna",3:"manoj"}
>>> a.pop(1);
'vandana'
>>> a
{2: 'joshna', 3: 'manoj'}
>>> a.popitem();
(3, 'manoj')
>>> a
{2: 'joshna'}
>>> del a[1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> del a[1]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    del a[1]
KeyError: 1
>>> a.clear()
>>> 
>>> a
{}
>>> a={1:"vandana",2:"joshna",3:"manoj"}