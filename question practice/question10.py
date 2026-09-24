#samrt electricity usage analyzer 
unit_hour=1.5
daily_hour=6.5
daily_units=unit_hour*daily_hour
monthly_units=daily_units*28
service_charge=75
print(monthly_units)
first_slab=100*2.50
second_slab=100*4
remaining_units=monthly_units-200
remaining_cost=remaining_units*6
total_bill=first_slab+second_slab+remaining_cost+service_charge
print(total_bill)

