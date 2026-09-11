bill=0
units=int(input("Enter number of units used: "))
if units<100:
    bill=units*2
    print(bill)

elif 100<=units<200:
    a=100*2
    b=units-100
    bill=b*3+a
    
    print(bill)

elif 200<=units<400:
    a=100*2
    b=100*3
    c=units-200
    bill=c*5+a+b
    
    print(bill)
  
else:
    a=100*2
    b=100*3
    c=200*5
    d=units-400
    bill=d*7+a+b+c
    print(bill)
  

if units>500:
    print("High Consumption")

if bill>2000:
    bill=bill+bill*5/100
    print(bill)    

            

