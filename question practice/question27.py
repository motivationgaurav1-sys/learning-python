def largest(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z
a=int(input())
b=int(input())
c=int(input())
result=largest(a,b,c)
print(result)    