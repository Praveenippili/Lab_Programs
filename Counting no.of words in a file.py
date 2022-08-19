words=0
f1=open("vandana1.txt","r")
data=f1.read()
lines=data.split()
words+=len(lines)
print(words)
