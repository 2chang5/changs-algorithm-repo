import sys
from collections import deque
sys.setrecursionlimit(100000)

w,h = int(),int()
realMap = []
visited = []
count = 0 
direction = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
answer = []

def dfs(y,x):
    global w,h,realMap,visited,count

    for i in range(8):
        ty,tx = y + direction[i][1],x+direction[i][0]
        if tx in range(w) and ty in range(h) and not visited[ty][tx] and realMap[ty][tx]:
            visited[ty][tx] = True
            dfs(ty,tx)



while True:
    
    count = 0

    w,h = map(int,sys.stdin.readline().rstrip().split())
    if w == h == 0 : break

    visited = [[False] * w for _ in range(h)]
    realMap = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(h)]

    for j in range(w):
        for k in range(h):
            if realMap[k][j] and not visited[k][j]:   
                dfs(k,j)
                count += 1
            

    answer.append(count)
    
for l in answer:
    print(l)


#따라서 해봤는데 드럽게 어렵다 이문제는 특히 여러번 해서 더어려운거같아 이런거지같으니


