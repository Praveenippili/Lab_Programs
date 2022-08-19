Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4]
>>> help(l)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> print(l);
[1, 2, 3, 4]
>>> l[0]
1
>>> l[-1]
4
>>> l[-4,-3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l[-4,-3]
TypeError: list indices must be integers or slices, not tuple
>>> l[-4:-3]
[1]
>>> l[:4]
[1, 2, 3, 4]
>>> l[3:]
[4]
>>> l[2:]
[3, 4]
>>> l[-3:-2]
[2]
>>> l1=[3,4,5]
>>> l2=[1,2,6]
>>> l=l1+l2;
>>> l
[3, 4, 5, 1, 2, 6]
>>> l.append(7);
>>> l
[3, 4, 5, 1, 2, 6, 7]
>>> l.append(9,6,7);
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l.append(9,6,7);
TypeError: list.append() takes exactly one argument (3 given)
>>> l.append[9,6,7];
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l.append[9,6,7];
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l.append([9,6,7]);
>>> l
[3, 4, 5, 1, 2, 6, 7, [9, 6, 7]]
>>> l.extend([1]);
>>> l
[3, 4, 5, 1, 2, 6, 7, [9, 6, 7], 1]
>>> l.extend([1,9,8]);
>>> l
[3, 4, 5, 1, 2, 6, 7, [9, 6, 7], 1, 1, 9, 8]
>>> l.insert(6,8);
>>> l
[3, 4, 5, 1, 2, 6, 8, 7, [9, 6, 7], 1, 1, 9, 8]
>>> del(0);
SyntaxError: cannot delete literal
>>> del(3);
SyntaxError: cannot delete literal
>>> del[0];
SyntaxError: cannot delete literal
>>> del[3];
SyntaxError: cannot delete literal
>>> del l[0];
>>> l
[4, 5, 1, 2, 6, 8, 7, [9, 6, 7], 1, 1, 9, 8]
>>> l.remove(4);
>>> l
[5, 1, 2, 6, 8, 7, [9, 6, 7], 1, 1, 9, 8]
>>> l.pop(3);
6
>>> l
[5, 1, 2, 8, 7, [9, 6, 7], 1, 1, 9, 8]
>>> del l(5);
SyntaxError: cannot delete function call
>>> del l[5];
>>> l
[5, 1, 2, 8, 7, 1, 1, 9, 8]
>>> l=m
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    l=m
NameError: name 'm' is not defined
>>> m=l;
>>> m
[5, 1, 2, 8, 7, 1, 1, 9, 8]
>>> l=m.copy()
>>> l.append(87)
>>> l
[5, 1, 2, 8, 7, 1, 1, 9, 8, 87]
>>> m
[5, 1, 2, 8, 7, 1, 1, 9, 8]
>>> m=l
>>> m
[5, 1, 2, 8, 7, 1, 1, 9, 8, 87]
>>> l
[5, 1, 2, 8, 7, 1, 1, 9, 8, 87]
>>> m.append(67)
>>> m
[5, 1, 2, 8, 7, 1, 1, 9, 8, 87, 67]
>>> l
[5, 1, 2, 8, 7, 1, 1, 9, 8, 87, 67]
>>> range(len(l));
range(0, 11)
>>> print("vandana",l);
vandana [5, 1, 2, 8, 7, 1, 1, 9, 8, 87, 67]
>>> print("vandana",l[i]);
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print("vandana",l[i]);
NameError: name 'i' is not defined
>>> for i in range(len(l));
SyntaxError: invalid syntax
>>> for i in range(len(l))
SyntaxError: invalid syntax
>>> 
>>> a=["vandana","joshna","manoj"]
>>> for i in a:
	print("hello",i);

	
hello vandana
hello joshna
hello manoj
>>> for i in a:
	print("hello",l[i]);

	
Traceback (most recent call last):
  File "<pyshell#65>", line 2, in <module>
    print("hello",l[i]);
TypeError: list indices must be integers or slices, not str
>>> t=(1,2,3,4,5);
>>> help(t)
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> print(t)
(1, 2, 3, 4, 5)
>>> t.count(2);
1
>>> t.index(2);
1
>>> x=list(t)
>>> x[0]=100
>>> t.tuple(x)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t.tuple(x)
AttributeError: 'tuple' object has no attribute 'tuple'
>>> t=tuple(x)
>>> print(t)
(100, 2, 3, 4, 5)
>>> s={1,2,3,4}
>>> print(s)
{1, 2, 3, 4}
>>> help(s)
Help on set object:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> print(s);
{1, 2, 3, 4}
>>> s1={4,5,6,7}
>>> s.union(s1)
{1, 2, 3, 4, 5, 6, 7}
>>> s
{1, 2, 3, 4}
>>> s.intersection(s1)
{4}
>>> s.difference(s1)
{1, 2, 3}
>>> s.update({1,7,8,9})
>>> print(s)
{1, 2, 3, 4, 7, 8, 9}
>>> s.update({1,7,2,9})
>>> s
{1, 2, 3, 4, 7, 8, 9}
>>> s.add(10)
>>> s
{1, 2, 3, 4, 7, 8, 9, 10}
>>> s[0]=20
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s[0]=20
TypeError: 'set' object does not support item assignment
>>> s(0)=20
SyntaxError: cannot assign to function call
>>> s[0]=20
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s[0]=20
TypeError: 'set' object does not support item assignment
>>> s{0}=20
SyntaxError: invalid syntax
>>> s.issubset(s);
True
>>> s1.issubset(s);
False
>>> s
{1, 2, 3, 4, 7, 8, 9, 10}
>>> s1
{4, 5, 6, 7}
>>> 