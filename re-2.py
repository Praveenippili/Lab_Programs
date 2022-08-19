import re
text="7672050862,9908420245,8666376261"
a=re.search(r"[0-9]+",text);
print(a)
