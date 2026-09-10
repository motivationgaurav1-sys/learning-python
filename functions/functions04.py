def f1(a,b):
  c=a+b
  print("sum is",c)

f1(3,5)
#f1(10,50,7) this will give error only 2 arguments are needed

def f2(a,b,d):
  c=a+b+d
  print("sum is",c)

f2(32,43,546) 
#f1(3,5) thi will give error because 3 atguments needed 

def f3(a,b,c=0):
  d=a+b+c
  print("Sum is",d)

f3(10,20)
f3(10,20,30)

#def f4(a,b=0,c): give synatx error
def f4(a,c,b=0):
  d=a+b+c
  print("Sum is",d)
f4(10,20,30)
f4(10,20)

def f5(a=0,b=0,c=0):
  d=a+b+c
  print(d)
f5(10,20,30)
f5()
f5(23,43,34)

def f6(a,b):
  print("a =",a,"b =",b)
f6(2,3)
f6(b=2,a=3)
f6(5,b=3)
#f6(a=6,3) error
#f6(2,a=3) #error a has 2 values
#f6(b=3,a) synatax error.

  

