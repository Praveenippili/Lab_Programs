number_of_words = 0
f1=open("anu.txt","r")
data = f1.read()
lines = data.split()
number_of_words += len(lines)
print(number_of_words)
