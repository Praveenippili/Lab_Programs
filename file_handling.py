#opening a file
f=open("dsp.txt")
f.close()
#opening file in read mode
f=open("dsp.txt","r")
print(f.read())
f.close()
#reading some characters in the file
f=open("dsp.txt","r")
print(f.read(10))
f.close()
#reading one line of the file
f=open("dsp.txt","r")
print(f.readline())
f.close()
#reading multiple lines
f=open("dsp.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
#loop through file line by line
f=open("dsp.txt","r")
for x in f:
  print(x)

#appending content to a file
f=open("dsp.txt","a")
f.write("    This is anu namala")
f.close()
f=open("dsp.txt","r")
print(f.read())

#overwriting the content
f=open("dsp.txt","w")
f.write("this is new content")
f.close()
f=open("dsp.txt","r")
print(f.read())


#deleting a file
import os
os.remove("pari.txt")
print("File is deleted")
