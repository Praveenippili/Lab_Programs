#Opening a file
"""f=open("file_pro.txt","r")
f.close()"""
#Opening file in read mode
"""f=open("file_pro.txt","r")
print(f.read())
f.close()"""
#Reading some characters in the file
"""f=open("file_pro.txt","r")
print(f.read(20))
f.close()"""
#Reading one line of the file
"""f=open("file_pro.txt","r")
#for single line
print(f.readline())
#For multiple lines
print(f.readline())
print(f.readline())
f.close()"""
#Loop through file line by line
"""f=open("file_pro.txt","r")
for x in f:
    print(x)"""
#Appending content to the file
"""f=open("file_pro.txt","a")
f.write("This is my family")
f.close()
f=open("file_pro.txt","r")
print(f.read())"""
#Overwriting content
"""f=open("file_pro.txt","w")
f.write("This is new content")
f.close()
f=open("file_pro.txt","r")
print(f.read())"""
#Deleting a file
"""import os
os.remove("file_pro.txt")
print("File is deleted")"""
#Swaping contents of a file
file1=open("fl1.txt","r")
file2=open("fl2.txt","r")
fl1=file1.read()
fl2=file2.read()
file1=open("fl1.txt","w")
file2=open("fl2.txt","w")
file1=file1.write(fl2)
file2=file2.write(fl1)

