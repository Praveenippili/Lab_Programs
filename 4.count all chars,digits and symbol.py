n=input("Enter a string:")
count1=0
count2=0
count3=0
for i in n:
  if(i.isalpha()):
    count1=count1+1
  elif (i.isdigit()):
    count2=count2+1
  else:
    count3=count3+1
print("Chars:",count1)
print("Digits:",count2)
print("Symbols:",count3)

    
