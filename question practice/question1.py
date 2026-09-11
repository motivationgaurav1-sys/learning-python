#plant growth analyzer.
plant_height=15.5
weeks=int(input("Number of weeks: "))
for i in range(weeks):
    if (plant_height)<20:
        growth=plant_height*12/100
        plant_height=growth+plant_height
    elif 20<=plant_height<40:
        growth=plant_height*8/100
        plant_height=growth+plant_height
    elif plant_height>=40:
        growth=plant_height*5/100
        plant_height=growth+plant_height
    
print(plant_height)        

