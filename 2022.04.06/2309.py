from itertools import combinations

little = []

for i in range(9):
    little.append(int(input()))

for j in combinations(little,7):
    if sum(j) == 100:
        for k in sorted(j):
            print(k)
        break    