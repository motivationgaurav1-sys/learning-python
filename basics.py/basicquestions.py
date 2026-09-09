x=int(input("Enter side of cube (cm): "))
surface_area=6*(x**2)
print("Total surface area of the cube is",surface_area,"cm2")

days=int(input("Enter number of days: "))
rate=int(input("Enter daily rate: "))
total_cost=days*rate
print("Total cost before discount: ",total_cost)
x=total_cost/10
print("Dicount (10%)",x)
print("Final amount to pay:",total_cost-x)



pop=int(input("Enter current populaton: "))
growth=int(input("Enter annual growth rate (%): "))
years=int(input("Enter numbr of years: "))
fp=pop*(1+growth/100)**years
print("Predicted population after",years, "years",int(fp))


current_plant_height=int(input())
average_plant_growth=float(input())
number_of_week=int(input())
total_growth=average_plant_growth*number_of_week
final_height=current_plant_height+total_growth
print(final_height)




