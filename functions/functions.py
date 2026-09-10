# normal way to calculate sqaure.
number=int(input("Enter a  number: "))
for e in range(1,number+1):
    print("Square of",e,"is",e**2)

#now if u want to calculate sqaure u have to write this code all again , here we use funtion
def square():
    n=int(input("Enter a number: "))
    for a in range(1,n+1):
        print("Square of",a,"is",a**2)


#now whenever u want to square a numbers upto any number just need to call function like this
square()
#u can call the function multiple times as ur need.

