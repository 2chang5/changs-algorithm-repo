import sys
from collections import deque

w,h = map(int,sys.stdin.readline().rstrip().split())

tomatoBox = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(h)]

startCheckAllTomatoIsReady = True

dayCount = 0

startTomato = []

direction = [(-1,0),(0,-1),(0,1),(1,0)]

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

        for k in range(4):
            ty,tx = y+direction[k][0],x+direction[k][1]
            if ty in range(h) and tx in range(w) and tomatoBox[ty][tx] == 0:
                tomatoBox[ty][tx] = 1
                tomatoCheckPoint.append((ty,tx))
    if tomatoCheckPoint :   
        needVisited.append(tomatoCheckPoint)
        
for l in range(w):
        for m in range(h):
            if tomatoBox[m][l] == 0:
                print(-1)
                exit()

print(dayCount-1)
   
# 문제에서 얻은 팁
# 중간에 검사안해도된다 -> 그냥 bfs는 한번 쭉 검사하고나면 모든데 다돌으니까 중간검사하면 오히려 시간복잡도 올라감 이런거 한번생각해보자
# 그리고 값넣어줄때 한번에 리스트로 묶어서 append할수있다 일수에 따라서 전염되는 모습이면 일수에 따라 묶어주고 하루하루 진행되는 느낌으로 for문 돌려주면된다.
# 그리고 조건값 잘 생각해보고 범위는 if문 안에서 체크하면되고 xy 반대로 쓰는거 랬갈리지 말자