def gdc(a,b):
    if a==0 and b==0:
        return "Value must be non zero"
    else:
        while b!=0:
            a,b=b,a%b
        return a    



a,b=map(int,input().split(","))
print(gdc(a,b))