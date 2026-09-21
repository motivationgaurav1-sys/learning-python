units=int(input())
bill=0
if units<=100:
    bill=units*2
elif 100<units<=200:
    exced_units=units-100
    bill=100*2
    bill=bill+exced_units*3
elif 200<units<=400:
    exced_units=units-200
    bill=100*3+100*2
    bill=bill+exced_units*5
elif units>400:
    exced_units=units-400
    bill=100*2+100*3+200*5
    bill=bill+exced_units*7
if bill>2000:
    bill=bill+bill*5/100
print(bill)
if units>500:
    print("High Consumption")    


