def second_largest(a):
    largest=float("-inf")
    second=float("-inf")

    for i in a:
        if i>largest:
            
            second=largest
            largest=i


        elif i<largest and i>second:
            second=i

    if second==float("-inf"):
        return "Not possible" 


    return second       




n=list(map(int,input().split(",")))
result=second_largest(n)
print(result)