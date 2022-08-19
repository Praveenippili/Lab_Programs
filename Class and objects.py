#Printing  Hello!world 
"""class vandana:
    def fun(self):
        print("Hello!World")
x=vandana()
x.fun()"""
#Program-2
"""class student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
    def func(self):
        print("Welcome")
x=student("Vandana")
x.display()
x.name
x.func()"""
#Program-3
"""class student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self):
        print(self.name)
        print(self.rno)
s1=student("Vandana",8)
s1.display()
s2=student("Joshna",24)
s2.display()"""
#Program-4
class student:
    def __init__(self,name,character):
        self.name=name
        self.character=character
    def display(self):
        print(self.name)
        print(self.character)
a=student("van&josh","sisters")
a.display()
b=student("Manoj&Vandana","brosis")
b.display()

