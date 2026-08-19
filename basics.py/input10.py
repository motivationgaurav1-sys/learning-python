print("ABC"+"CDEF")
X="ABC"
Y="ABC"
print(X+Y)
#5+"5" WILL GIVE ERROR BECOUSE IN PYTHON WE CAN ONLY ADD INT + INT OR STR+ STR.
x=input()
print(x) #input always return str value.
#print(x+10) here it gives error because 5is in str form "5".
print(int(x)+10) # this is type conversion.
#x=5+"5" will give error becuse one of them is str type and one is int type.
x=str(5)+"5" #here we put commant before 5 str that to convern 5 to "5".
print(x) #here the and will be '55' not 10 because now they are str type value not int type.
y=5+int("5")
print(y) #here the ans will be 10 becuse they are int type they will add.
x=4.5
print(int(x)) # here it covert datatype from float to str.
a=5
print(float(a)) #now 5 will be  converted into float type.
x="abx"
print(type(x))
#print(int(x)) it will give error because the inside x is not of int type not digit.
x="245"
print(type(x)) #here type of  x is str and we can also ocnvert it into int type because value is valid .
print(int(x))
x="2.34"
#print(int(x)) it will also give error because the value in side x is of float type we can not convert it into int type.
x=2.4
print(complex(x))
print(bool(x)) # will give true.
x="abc"
print(bool(x)) #will also true because because all non empty strings are true.
#x="ab12" this can also not be convert into int type becuse there is still ab not digit.
x=25 # i have to convert it to binary 
print(bin(x)) # when ever we convert a number into binary , after converting it add 0b prefix in the number like 0b
print(type(x))
y=bin(x)
print(type(y))
print(oct(x)) #add 0o as prefix in answer 
# one inportant thing for x the type is int becasue we put x=25 but for type of bin(x) and oct(x) is str because it gives output as a str.
