days = int(input("Number of days: "))
limit = float(input("Maximum waste percentage: "))

for i in range(days):
    prepared = int(input("Meals prepared: "))
    served = int(input("Meals served: "))
    leftovers = prepared - served
    waste_percent = leftovers / prepared * 100

    print("Wastage:", f"{waste_percent:.1f}%")

    if waste_percent > limit:
        print("Waste limit exceeded")