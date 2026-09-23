#Monthly Savings Predictor
salary=30000
monthly_expenses=18000
expense_increase=0
months=int(input("Months: "))
total_savings=0


for i in range(1,months+1):
    monthly_savings=salary-monthly_expenses
    expense_increase=monthly_expenses*5/100
    monthly_expenses=monthly_expenses+expense_increase
    if i%3==0:
        salary=salary+salary*10/100
    if monthly_savings>15000:
        invest=monthly_savings*30/100
        final_savings=monthly_savings-invest
    elif 10000<=monthly_savings<=15000:
        invest=monthly_savings*20/100
        final_savings=monthly_savings-invest
    else:
        invest=monthly_savings*10/100
        final_savings=monthly_savings-invest
    total_savings=total_savings+final_savings
print(final_savings)   
print(total_savings)                     
