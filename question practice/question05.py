#plant growth analyzer
plant_height=float(input("height of the plant: "))
weeks=int(input("number of weeks: "))
for a in range(weeks):
    if plant_height<20:
        growth=plant_height*12/100
        plant_height=plant_height+growth
    elif 20<=plant_height<40:
        growth=plant_height*8/100
        plant_height=plant_height+growth
    elif plant_height>=40:
        growth=plant_height*5/100
        plant_height=plant_height+growth

print(plant_height)
                
