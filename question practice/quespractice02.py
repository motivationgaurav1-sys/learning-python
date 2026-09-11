#check weather a given number is leap year or not.
year=int(input())
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap year")
else:
    print("Not a Leap Year")    


#check weather a given number is positive or negative or zero.
x=int(input())
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print("Zero")            



#write a pyhton script to accept one complex number from the user and display the gretaer part between real and imaginary.
x=complex(input())
real=x.real
imaginary=x.imag
if real>imaginary:
    print("greater  number is",real)
else:
    print("greater number is",imaginary)    




#write a pyhton script to write python 5 times
i=1
while i<=5:
    print("Rana")
    i+=1


#print n natural numbers
num=int(input()) 
i=1
if i<=num:
    print(i)
    i+=1  


#sum of first n natural numbers
num=int(input())
i=1
s=0
while i<=num:
    s=s+i
    i+=1
print(s)   



#given number is prime or not.
num=int(input())
if num<=1:
    print("Not prime")
else:
    i=2
    while i<num:
        if num%i==0:
            print("Not prime")
            break
        i+=1
    else:
        print("Prime")



#print unicode of each charchter
x=input()
for a in x:
    print(a,ord(a))



#lcm calculate
num1=int(input())
num2=int(input())
LCM=max(num1,num2)
while True:
    if LCM%num1==0 and LCM%num2==0:
        print(LCM)
        break
    LCM+=1


#or
import math
n1=int(input())
n2=int(input())
print(math.lcm(n1,n2))    