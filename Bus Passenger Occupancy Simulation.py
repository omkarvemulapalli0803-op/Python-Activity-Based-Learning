passengers = 0
capacity = int(input("Bus capacity: "))
stops = int(input("Number of stops: "))

for stop in range(1, stops + 1):
    boarding = int(input("Passengers boarding: "))
    alighting = int(input("Passengers alighting: "))
    passengers += boarding - alighting

    if passengers > capacity:
        print("Capacity exceeded at stop", stop)
    else:
        print("Passengers at stop", stop, ":", passengers)