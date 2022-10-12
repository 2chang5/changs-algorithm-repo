import sys
from collections import deque

w,h = map(int,sys.stdin.readline().rstrip().split())

tomatoBox = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(h)]

startCheckAllTomatoIsReady = True

dayCount = 0

startTomato = []

direction = [(-1,0),(0,-1),(0,1),(1,0)]

theDayBeforeTomato = [tomatoBox[o][:] for o in range(h)]

#일단 토마토 다익었나 확인 + startTomao 확인
for i in range(w):
    for j in range(h):
        if tomatoBox[j][i] == 0:
            startCheckAllTomatoIsReady = False
        if tomatoBox[j][i] == 1:
            startTomato.append((j,i))

if startCheckAllTomatoIsReady :
    print(0)
    exit()

#토마토 탐색 bfs
needVisited = deque()

needVisited.append(startTomato)

while needVisited :

    dayList = needVisited.popleft()
    
     #count day 늘리기
    dayCount += 1

    tomatoCheckPoint = []

    for n in dayList:
        y,x = n

        allTomatoIsReady = True
        for k in range(4):
            ty,tx = y+direction[k][0],x+direction[k][1]
            if ty in range(h) and tx in range(w) and tomatoBox[ty][tx] == 0:
                tomatoBox[ty][tx] = 1
                tomatoCheckPoint.append((ty,tx))
        
    needVisited.append(tomatoCheckPoint)
        
    # 전날과 같은지 체크 
    if theDayBeforeTomato == tomatoBox:
        print(-1)
        exit()
    theDayBeforeTomato = [tomatoBox[o][:] for o in range(h)]
    #다 1됐는지 체크
    for l in range(w):
        for m in range(h):
            if tomatoBox[m][l] == 0:
                allTomatoIsReady = False
    if allTomatoIsReady:
        print(dayCount)
        exit()
   
    