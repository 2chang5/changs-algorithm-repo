import sys
sys.setrecursionlimit(100000)

w,h = map(int,sys.stdin.readline().rstrip().split())

tomatoBox = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(h)]

startCheckAllTomatoIsReady = True

dayCount = 0

tomatoList = []

tempTomatoList = []

direction = [(-1,0),(0,-1),(0,1),(1,0)]


for i in range(w):
    for j in range(h):
        if tomatoBox[j][i] == 0:
            startCheckAllTomatoIsReady = False
        if tomatoBox[j][i] == 1:
            tempTomatoList.append((j,i))


if startCheckAllTomatoIsReady:
    print(0)
    exit()

tomatoList.append(tempTomatoList)
tempTomatoList = []

def dfs(y,x) :
    
    global tomatoBox,direction,tempTomatoList

    for i in range(4):
        ty,tx = y+direction[i][0], x + direction[i][1]
        if ty in range(h) and tx in range(w) and tomatoBox[ty][tx] == 0:
            tomatoBox[ty][tx] = 1
            tempTomatoList.append((ty,tx))
            
            

for i in tomatoList:
    for j in i:
        dfs(j[0],j[1])
    
    dayCount +=1

    if tempTomatoList:
        tomatoList.append(tempTomatoList)
        tempTomatoList = []

for i in range(w):
    for j in range(h):
        if tomatoBox[j][i] == 0:
            print(-1)
            exit()

print(dayCount-1)