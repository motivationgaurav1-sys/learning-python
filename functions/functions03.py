#ways to define a function
#1. take nothing , return nothing 
def add():
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    c=a+b
    print("Sum is",c)


add()

#2. take something, return nothing

def sum(c,d):
    z=c+d
    print("Sum is",z)

sum(10,50)


#3.take nothing, return something.
def f1():
    x=int(input("Enter a number:"))
    y=int(input("Enter a number:"))
    w=x+y
    #print("Sum is",w)
    return w
s=f1()
print("Sum is",s)


#take something, return something
def f2(a,b):
    c=a+b
    return c
x=f2(10,20)
print(x)