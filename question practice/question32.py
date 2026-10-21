def reverse(x):
    l1=x.split()
    l2=[]
    for a in l1:
        c=a[::-1]
        l2.append(c)
    x=" ".join(l2)
    return x    
a=input()
result=reverse(a)
print(result)