x=["a","b","c","d"]
y=[1,2,3,4]
d=dict(zip(x,y))
print(d)

#another method
d=dict()
for i in range(len(x)):
  d.update({x[i]:y[i]})
print(d)
  
