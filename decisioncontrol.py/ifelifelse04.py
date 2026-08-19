"""write a program  to print grade
obtained in a test, take marks obtained 
from user and display the grade."""
x=int(input("enter your marks "))
if 90<x<=100:
    print("A grade")
elif 80<x<=90:
    print("B grade")
elif 70<x<=80:
    print("C grade")    
elif 60<x<=70:
    print("D grade")
elif 50<=x<=60:
    print("E grade")
else:
    print("F grade")       
