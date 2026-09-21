#smart rental calculator
rental_days=int(input("Rental days: "))
late_days=int(input("Late days: "))
rent=0
security_deposit=2000
if rental_days<=7:
    rent=500*rental_days
    rent=rent+security_deposit+late_days*300
elif 7<rental_days<=14:
    rent=rental_days*500
    discount=rent*10/100
    rent=rent-discount+security_deposit+late_days*300
elif rental_days>14:
    rent=rental_days*500
    discount=rent*20/100
    rent=rent-discount+security_deposit+late_days*300
print(rent)    


