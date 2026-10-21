def unique(x):
    l2=[]
    for a in x:
        if a not in l2:
            l2.append(a)
    return l2        
    
a=list(map(int,input().split(",")))
result=unique(a)
print(result)
