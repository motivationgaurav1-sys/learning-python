def vowel(x):
    count=0
    for i in x.lower():
        if i in "aeiou":
            count+=1
    return count
a=input()
result=vowel(a)
print(result)        