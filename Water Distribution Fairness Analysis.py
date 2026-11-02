areas = int(input("Number of areas: "))
days = int(input("Number of days: "))
results = []

for i in range(areas):
    name = input("Area name: ")
    demand = float(input("Daily water demand: "))
    supplied = 0

    for day in range(days):
        supplied += float(input(f"Water supplied on day {day + 1}: "))

    shortage = demand * days - supplied
    results.append((shortage, name))

results.sort(reverse=True)

for shortage, name in results:
    print(name, "total shortage:", shortage)

print("Most underserved area:", results[0][1])