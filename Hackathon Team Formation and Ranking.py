teams = []
count = int(input("Number of teams: "))

for i in range(count):
    name = input("Team name: ")
    members = int(input("Number of members: "))
    scores = [int(input("Round score: ")) for _ in range(3)]

    if 2 <= members <= 5:
        teams.append((sum(scores), name))
    else:
        print(name, "has an invalid team size")

teams.sort(key=lambda team: (-team[0], team[1]))

for rank, (score, name) in enumerate(teams, start=1):
    print(rank, name, "Score:", score)