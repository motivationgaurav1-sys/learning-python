def is_armstrong(n):
    if n==0:
        return "Armstrong"
    s=0
    count=0
    y=n
    while y>0:
        x=y%10
        count+=1
        y=y//10

    orignal=n

    while n>0:
        a=n%10
        s=s+a**count
        n=n//10
    if s==orignal:
        return "Armstrong"
    else:
        return "Not Armstrong"    
    
    






n=int(input())
print(is_armstrong(n))