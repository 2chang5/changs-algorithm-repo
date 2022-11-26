import sys

t = int(sys.stdin.readline().rstrip())
answer = []


def oneTime():
    n = int(sys.stdin.readline().rstrip())
    candidate = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

    candidate.sort(key=lambda x: x[0])

    temp = candidate[0]
    tempAnswer = n

    del(candidate[0])

    for i in candidate:
        if temp[1] > i[1]:
            temp = i
        else:
            tempAnswer -= 1

    answer.append(tempAnswer)


for i in range(t):
    oneTime()

for i in answer:
    print(i)
