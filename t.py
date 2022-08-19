Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="my name is \n vandana"
>>> x.isprintable();
False
>>> c=" "
>>> c.isprintable();
True
>>> x="my name is  vandana"
>>> x1="my name is vandana"
>>> x1.isprintable();
True
>>> x.isspace();
False
>>> a="   "
>>> a.isspace();
True
>>> a1="\n \n \n"
>>> a1.isspace();
True
>>> a2="\v \v"
>>> a2.isspace();
True
>>> x.isspace();
False
>>> s="vandana"
>>> s.istitle();
False
>>> s1="VandaNa"
>>> s1.istitle();
False
>>> s2="Vandana"
>>> s2.istitle();
True
>>> a.isupper();
False
>>> a3="VANDANA"
>>> a3.isupper();
True
>>> list1=['1','2','3','4']
>>> r="-"
>>> s.join(list1);
'1vandana2vandana3vandana4'
>>> r.join(list1);
'1-2-3-4'
>>> str="vandana"
>>> length=4;
>>> str.rjust(length);
'vandana'
>>> fillchar="@"
>>> str.rjust(length,fillchar);
'vandana'
>>> length1=9;
>>> str.rjust(length,fillchar);
'vandana'
>>> string='love'
>>> length=8
>>> fillchar='*'
>>> string.rjust(length,fillchar);
'****love'
>>> fillchar='#'
>>> string.rjust(length,fillchar);
'####love'
>>> string.rjust(length);
'    love'
>>> string.ljust(length);
'love    '
>>> string.ljust(length,fillchar);
'love####'
>>> a5="VAndAnA"
>>> a5.lower();
'vandana'
>>> string1="    vandana"
>>> string1.lstrip();
'vandana'
>>> str1="+++++x....y!!z* vandana"
>>> str1.lstrip("+.!*xyz");
' vandana'
>>> y="vandana is good"
>>> y.partition('is');
('vandana ', 'is', ' good')
>>> y.partition('bad');
('vandana is good', '', '')
>>> y1="vandana is a good and vandana is a beautiful"
>>> y1.replace("vandana","joshna");
'joshna is a good and joshna is a beautiful'
>>> y1.replace("vandana","manoj",1);
'manoj is a good and vandana is a beautiful'
>>> y1.replace("vandana","manoj",2);
'manoj is a good and manoj is a beautiful'
>>> 