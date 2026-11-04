locations = int(input("Number of locations: "))

for i in range(locations):
    name = input("Location name: ")
    received = int(input("Quantity received: "))
    distributed = int(input("Quantity distributed: "))
    damaged = int(input("Quantity damaged: "))
    remaining = int(input("Recorded remaining stock: "))
    minimum = int(input("Minimum stock needed: "))

    expected = received - distributed - damaged
    discrepancy = remaining - expected
    replenish = max(0, minimum - remaining)

    print(name, "Discrepancy:", discrepancy, "Replenish:", replenish)
