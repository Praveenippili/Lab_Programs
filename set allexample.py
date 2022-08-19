Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={1,2,3,4,5}
s.discard(3)
s
{1, 2, 4, 5}
s.remove(5)
s
{1, 2, 4}
s.discard(6)
s
{1, 2, 4}
s.remove(8)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.remove(8)
KeyError: 8
s.pop()
1
s
{2, 4}
s.pop()
2
s.pop()
4
s
set()
s.pop()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.pop()
KeyError: 'pop from an empty set'
s={1,2,3,4,5}
s.clear()
s
set()
s.add(1)
s
{1}
s.add(2,4)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.add(2,4)
TypeError: set.add() takes exactly one argument (2 given)
s.add(3)
s
{1, 3}
s.add(2)
s
{1, 2, 3}
s.add(4)
s
{1, 2, 3, 4}
s.update([1],[6])
s
{1, 2, 3, 4, 6}
s.update([7,9]{12,34,52})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.update([7,9],{12,34,52})
s
{1, 2, 3, 4, 34, 6, 7, 9, 12, 52}
len(s)
10
max(s)
52
min(s)
1
sum(s)
130
s.any()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s.any()
AttributeError: 'set' object has no attribute 'any'
any(s)
True
all(s)
True
a={  }
any(a)
False
all(a)
True
s.sorted()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.sorted()
AttributeError: 'set' object has no attribute 'sorted'
sorted(s)
[1, 2, 3, 4, 6, 7, 9, 12, 34, 52]
s1={1,2,3}
s2={4,5,6,}
set1.union(set2)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    set1.union(set2)
NameError: name 'set1' is not defined. Did you mean: 'set'?
s1.union(s2)
{1, 2, 3, 4, 5, 6}
s1.intersection(s2)
set()
s3={3,6,7}
s2.intersection(s3)
{6}
s1.difference(s2)
{1, 2, 3}
s1.difference(s3)
{1, 2}
s1.symetric_difference(s2)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s1.symetric_difference(s2)
AttributeError: 'set' object has no attribute 'symetric_difference'. Did you mean: 'symmetric_difference'?
s1.symmetric_difference(s2)
{1, 2, 3, 4, 5, 6}
s1.symmetric_difference(s3)
{1, 2, 6, 7}
s1=s2.copy()
s1
{4, 5, 6}
s2
{4, 5, 6}
s1.isdisjoint(s2)
False
s1.isdisjoint(s3)
False
s1={}
s2{}
SyntaxError: invalid syntax
s2={}
s2.isdisjoint(s2)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s2.isdisjoint(s2)
AttributeError: 'dict' object has no attribute 'isdisjoint'
set1={2,3,4}
set2={5,6,7}
set1.isdisjoint(set2)
True
set3={2,7,8}
set1.isdisjoint(set3)
False
set4={3,4}
set1.issubset(set4)
False
set4.issubset(set1)
True
set5={2,3,4}
set1.issuperset(set5)
True
set1.issuperset(set2)
False
1 in set1
False
2 in set1
True
1 not in set1
True
2 not in set2
True
for i in {3,2,4,1}
SyntaxError: expected ':'
for i in {3,2,4,1}:
    print(i)

    
1
2
3
4
{frozenset([1,2]:3}
 
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
{frozenset([1,2]:3)}
 
SyntaxError: invalid syntax
