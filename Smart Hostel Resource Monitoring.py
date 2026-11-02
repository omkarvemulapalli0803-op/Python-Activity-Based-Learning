rooms = int(input("Number of rooms: "))
threshold = float(input("Usage threshold: "))
floor_totals = {}

for i in range(rooms):
    floor = input("Floor: ")
    room = input("Room number: ")
    electricity = float(input("Electricity used: "))
    water = float(input("Water used: "))

    charge = electricity * 8 + water * 2
    floor_totals[floor] = floor_totals.get(floor, 0) + electricity + water

    print(room, "charge:", charge)

    if electricity + water > threshold:
        print("Usage threshold exceeded")

print("Usage by floor:", floor_totals)