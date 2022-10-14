import sys
from collections import deque
import itertools

h,w = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(h)]

space =[]

virus = []

direction = [(-1,0),(0,-1),(0,1),(1,0)]

answer = 0

for i in range(h):
    for j in range(w):
        if graph[i][j] == 0:
            space.append((i,j))
        if graph[i][j] == 2:
            virus.append((i,j))

#벽 세울 경우의수
wallList = list(itertools.combinations(space,3))

#벽 경우의수 안에서
for i in wallList:
    tempGraph = [graph[j][:] for j in range(h) ]
    
    spaceCount = 0

    # 벽세우기
    for k in i:
        tempGraph[k[0]][k[1]] = 1

    # bfs 돌리기
    bfsQueue = deque()

    bfsQueue.append(virus)

    while bfsQueue:
        
        checkPoint = []

        day = bfsQueue.popleft()

        for l in day:
            y,x = l

            for m in range(4):
                ty,tx = y+direction[m][0],x+direction[m][1]
                if ty in range(h) and tx in range(w) and tempGraph[ty][tx] == 0:
                    tempGraph[ty][tx] = 2
                    checkPoint.append((ty,tx))

        if checkPoint:
            bfsQueue.append(checkPoint)

    
    for n in range(h):
        for o in range(w):
            if tempGraph[n][o] == 0:
                spaceCount += 1
    
    if spaceCount > answer:
        answer = spaceCount

print(answer)

# 맞췄다 이거 시간복잡도 생각하는 문제 
            
        

