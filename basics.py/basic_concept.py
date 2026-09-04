#just practicing some previous concept questions day 1 to day 5 ...
x=5
print(str(x))
print(type(x))
print(float(x))
print(complex(x))
print("hello world")


a=5
b=6
c="ram"
print(a,b,c)
print(a,b,c,end=" ")
print(a,b,c,sep="#")
print(a,b,c,sep="-",end="|")
print("hello")


import list35 #import file 

import keyword
print(keyword.kwlist)
print("there are total",len(keyword.kwlist),"keywords in pyhton")



print(3/4)
print(10/5)
print(10.5/2)  #true division factor always gives answer in float type.
# if we have to calculate the power we use **
print(4**5)# 4 li power 5 kya h 4^5.
#there is also a nother type of division that is floor division in that i always give answer acoording to data type .. 
print(4//2)
print(10//2)
print(11//2)
print(3//4)
#if both numbers are int answer will be in int only but iF any of them or both are of float type then answer will be in float type but after.there will always be 0 it only gives value of before decimal.
print(3.0//4)
print(3.0//3.0)
print(5.0//5)
#now for % it give simple direct answer the reminder .
print(5%2)
print(55.2%6)
#relationla operator
print(3>4)
print(not 3>4)
print(3>0 and 4>0) #both should be true for getting output true.
print(3>0 or 4>0)#even if one is true output will be true.
print("seeta" or "geeta") #here answer seeta is coorect ans true so seeta prints because output comes from seeta
print("seeta" and "geeta") #here answer depends on geeta either she is true or false so the output will be geeta.beacuse it is also correct both are string.
#non empty string and non zero number is true but empty string and zero is false.
print(0 or 5) # oneof them is true non zero answer comes from 5
print(0 and 5)# false because one of them is false answer comes from 0
#identity operator
y=5
x=5
print(id(x))
print(x is y)
print(x is not y)
print(not x is not y)
#membership operator only for iterable 
y="my sir g"
print("ys" in y) # false becuse there is space between y and s
print("si" in y)
#input 
x=input()
print(x)
print(type(x)) #here ans will be in str because normally if u taek input from user it will always return in str type value . i u have to take in any data type u have to mention it like int(input()) to take input in int.
#type conversion
#x=5+"5" give error becuse both are differ data types
print(5+int("5"))
print(str(5)+"5")
#x="234" can not be converted into int because it is stored in str give error
x=234
print(float(x))
x=2.34
print(int(x))
x=55
print(bin(x))#to find binary of that number.#it will always add 0b in answer as a prefix.
print(oct(x)) #it divided the number by 8 repeatedly AND 0o add as prefix
print(hex(x)) # it divide the number by 16 repeatedly.and 0x add as prefix
print(ord("a")) # give unicode of a .
print(chr(55))#provide number alloted to this charcter



#if 
x=int(input())
if x>0:
  print("positive")
if x<=0:
  print("non positive") 


   
#if else 
x=int(input("enter a number: "))
if x>0:
  print("Positive")
else:
  print("Non Positive")



#if elif else
x=int(input("Enter marks: "))
if x>100:
  print("invalid marks")
elif x>90:
  print("A+ grade") 
elif 80 <= x <= 90: 
  print("B+ grade")
else:
  print("fail")


   
#single line if else.   
print("Even") if int(input())%2==0 else print("Odd")



#while loop
i=0
while i<5:
  print("rana")
  i+=1


#while loop  
x=int(input())
i=1
while i<=x:
    print(i)
    i+=1

#while loop
x=int(input())
i=1
s=0
while i<=x:
  s=s+i
  i+=1
print("sum is",s)  

#while and if
x=int(input("Enter a number:  "))
i=2
while i<x:
  if x%i==0:
    print("not prime")
    break
  i+=1
if i==x:
  print("Prime")

x="Gauravpundir"
for a in x:
  print(a,sep="-")
x=int(input())
print(chr(x))

x=input()
print(ord(x))


