def sum(x):
    if x>=0:
        s=0
        while x>0:
            a=x%10
            s+=a
            x=x//10
        return s    





a=int(input())
result=sum(a)
print(result)