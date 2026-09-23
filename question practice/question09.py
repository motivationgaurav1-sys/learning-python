print("Enter marks of 5 subjects: ")
sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
list1=[sub1,sub2,sub3,sub4,sub5]
sum=sum(list1)
print("sum:",sum)
minimum=min(list1)
print("min:",minimum)
maximum=max(list1)
print("max:",maximum)
p=sum/500*100
failed=0
for a in list1:
    if a<40:
        failed+=1
print("failed:",failed) 

if failed>0:
    print("fail")
else:
    print("percentage:")    

    if p>=90:
        print("A+")
    elif 80<=p<90:
        print("A") 
    elif 70<=p<80:
        print("B")
    elif 60<=p<70:
        print("C")
    elif 50<=p<60:
        print("D")
    else:
        print("FAIL")                  
      
      
