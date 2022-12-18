import sys
from collections import deque
import itertools
from copy import deepcopy


def maxGraph(graph):
    temp = 0
    for i in graph:
        maxInRow = max(i)
        if maxInRow > temp:
            temp = maxInRow

    return temp


input = sys.stdin.readline

t = int(input().rstrip())

answer = []

for sihangNumber in range(t):
    n, m, k = map(int, input().rstrip().split())

    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

    direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    move = itertools.combinations_with_replacement(direction, k)

    conclusion = 0

    for moveElemnet in move:

        tempGraph = deepcopy(graph)

        startQueue = []

        for w in range(m):
            for h in range(n):
                if tempGraph[h][w] != 0:
                    startQueue.append((h, w))

        bfsQueue = deque()

        bfsQueue.append(startQueue)

        tempMoveElement = deque(moveElemnet)

        while tempMoveElement:

            secondState = bfsQueue.popleft()

            directionNow = tempMoveElement.popleft()

            if directionNow == (-1, 0):
                secondState.sort(key=lambda v: v[0])
            if directionNow == (1, 0):
                secondState.sort(key=lambda v: v[0], reverse=True)
            if directionNow == (0, -1):
                secondState.sort(key=lambda v: v[1])
            if directionNow == (0, 1):
                secondState.sort(key=lambda v: v[1], reverse=True)

            checkPoint = []

            for i in secondState:
                y, x = i
                ty, tx = y + directionNow[0], x + directionNow[1]
                if (not (ty in range(n))) or (not (tx in range(m))):
                    pass
                else:
                    tempGraph[ty][tx] += tempGraph[y][x]
                    tempGraph[y][x] = 0
                    checkPoint.append((ty, tx))

            if checkPoint:
                bfsQueue.append(checkPoint)
            else:
                maxNumber = maxGraph(tempGraph)
                if conclusion < maxNumber:
                    conclusion = maxNumber
                break

            maxNumber = maxGraph(tempGraph)
            if conclusion < maxNumber:
                conclusion = maxNumber

    answer.append(str(sihangNumber+1)+" "+str(conclusion))

for i in answer:
    print(i)