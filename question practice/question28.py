def factorial(x):
    fact=1
    if x>=0:
        for i in range(1,x+1):
            fact*=i
        return fact
    else:
        return "Enter a Non Negative Number"   
n=int(input("Enter a number: ")) 
result=factorial(n)
print(result)  
