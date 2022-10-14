import sys
from collections import deque
from tabnanny import check

input = sys.stdin.readline

n,k = map(int,input().rstrip().split())

graph = [list(map(int,input().rstrip().split())) for _ in range(n)]

s,ax,ay = map(int,input().rstrip().split())

direction = [(-1,0),(0,-1),(0,1),(1,0)]

#처음상태 인데 튜플들 들어갈꺼고 그거 sort 기준 항상 바이러스 넘버대로
startQueue = []

#처음 상태 넣기
for w in range(n):
    for h in range(n):
        if graph[h][w] != 0:
            startQueue.append((graph[h][w],(h,w)))

startQueue.sort(key = lambda v: v[0])

secondCount = 0

bfsQueue = deque()

bfsQueue.append(startQueue)

while bfsQueue:

    secondState = bfsQueue.popleft()

    if secondCount >= s:
        print(graph[ax-1][ay-1])
        exit()

    checkPoint = []

    for i in secondState:
        y,x = i[1]
        for j in range(4):
            ty,tx = y+direction[j][0],x+direction[j][1]
            if ty in range(n) and tx in range(n) and graph[ty][tx] == 0 :
                graph[ty][tx] = i[0]
                checkPoint.append((i[0],(ty,tx)))

    if checkPoint:
        bfsQueue.append(checkPoint)

    secondCount += 1
    

print(graph[ax-1][ay-1])

#와 진짜 조건을 잘읽어야한다 이건 진짜 그냥 뭐 안풀릴때는 조건을 꼼꼼히 읽어보자
#애초에 s가 0일떄는 bfs돌면 안됐는데 한바뀌 무조건 돌고 시작하게해서 털림
#그리고 3중for문은 시간복잡도 진짜 잘나니까 시간복잡도 잡자
