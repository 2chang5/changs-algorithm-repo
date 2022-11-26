import sys

n, a, b = map(int, sys.stdin.readline().rstrip().split())

teams = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

sys.stdin.readline().rstrip()

teams.sort(key=lambda x: (abs(x[1] - x[2]), min(x[1], x[2])))

roomIndex = {1: a, 2: b}

answer = 0

equal = []

for i in teams:
    if i[1] > i[2]:
        bigger = i[1]
        biggerRoom = 1
        smaller = i[2]
        smallerRoom = 2
    elif i[1] < i[2]:
        bigger = i[2]
        biggerRoom = 2
        smaller = i[1]
        smallerRoom = 1
    else:
        equal.append(i)
        continue

    for j in range(i[0]):
        if roomIndex[smallerRoom] > 0:
            roomIndex[smallerRoom] -= 1
            answer += smaller
        else:
            roomIndex[biggerRoom] -= 1
            answer += bigger

for i in equal:
    answer += [0] * i[1]

print(answer)
