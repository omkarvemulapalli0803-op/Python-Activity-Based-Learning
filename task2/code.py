routes = int(input("Number of routes: "))
capacity = int(input("Passengers per bus: "))
max_buses = int(input("Maximum buses per route: "))

for route in range(1, routes + 1):
    demand = int(input(f"Passengers on route {route}: "))

    buses_needed = (demand + capacity - 1) // capacity
    buses_used = min(buses_needed, max_buses)
    unserved = max(0, demand - buses_used * capacity)

    print("Buses used:", buses_used)
    print("Unserved passengers:", unserved)
