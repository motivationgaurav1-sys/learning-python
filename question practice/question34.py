def analyser(x):
    count=0
    for a in x:
        if a>=40:
            count+=1
    return count
n=list(map(int,input().split(",")))
result=analyser(n)
print(result)        