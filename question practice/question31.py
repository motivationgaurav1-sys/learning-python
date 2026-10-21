def prime(x):
    if x>1:
        for n in range(2,x):
            if x%n==0:
                return "Not a Prime"
        return "Prime"
    else:
        return "Not a Prime"

n=int(input())
result=prime(n) 
print(result)           
