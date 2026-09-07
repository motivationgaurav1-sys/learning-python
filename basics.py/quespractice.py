# calculate area of triangle.
x=int(input("Height: "))
y=int(input("Width: "))
Area=x*y
print("Area of Rectangle is",Area)

#calculat simple interest.
p=float(input("Principle: "))
r=float(input("Rate: "))
t=float(input("Time: "))
simple_interest=p*r*t
print("Simple Interest is ",simple_interest)


#remove last digit of a given number.
x=int(input("Enter a number: "))
print("Number is",x//10)


#swap data of variables.
x=input()
y=input()
x,y=y,x
print("x is",x,"y is",y)


#check weather a number is divisible by 5 or not .
x=int(input("Enter a number: "))
if x%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")    


#print given words in dictionary order
word1=input()
word2=input()
if word1<word2:
    print(word1)
    print(word2)
else:
    print(word2)
    print(word1)    


#check the given number is of three digtit or not 
x=int(input())
if 100<=x<=999:
    print("Three digit number")
else:
    print("Not three digit number")        