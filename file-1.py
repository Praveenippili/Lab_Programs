file=open("sis.txt","w")
print("my sis is my life")
file.close()
file=open("sis.txt","a")
file.write("akka miss u")
file.close()
file=open("sis.txt","r")
print(file.read())
file.close()