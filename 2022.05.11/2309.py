import itertools

height = []

ans = []

for i in range(9):
    height.append(int(input()))

selected = itertools.combinations(height,7)

for j in selected:
    if sum(j) == 100 :
        ans = sorted(j)
        break

for k in ans:
    print(k)