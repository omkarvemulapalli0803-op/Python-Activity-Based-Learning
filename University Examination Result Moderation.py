subjects = int(input("Number of subjects: "))
maximum = 100
adjustment = int(input("Moderation marks to add: "))

results = []

for i in range(subjects):
    name = input("Subject name: ")
    original = int(input(f"Original mark for {name} (0-100): "))

    if original < 0 or original > maximum:
        print("Invalid mark. Enter a mark from 0 to 100.")
    else:
        moderated = min(original + adjustment, maximum)
        results.append((name, original, moderated))

for name, original, moderated in results:
    print(name, "Original:", original, "Moderated:", moderated)