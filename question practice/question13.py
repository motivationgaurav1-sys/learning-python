#hostel food budget
total_balance=6000
per_day=35+60+55
print(per_day)
total_days=30
not_mess=8
in_mess=total_days-not_mess
outside_food_cost=not_mess*220
snacks=450
total_food_expenditure=in_mess*per_day+snacks+outside_food_cost
print(total_food_expenditure)
remaining_money=total_balance-total_food_expenditure
print(remaining_money)
avg=total_food_expenditure/total_days
print(avg)