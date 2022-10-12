import sys
from collections import deque

w,h = int(),int()
realMap = []
visited = []
count = 0 
direction = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
answer = []

def bfs(y,x):
    global w,h,realMap,visited,count

    if not realMap[y][x] or visited[y][x]: return 

    need_visit = deque()

    need_visit.append((y,x))  

    count += 1

    while need_visit:
        y,x = need_visit.popleft()

        for i in range(8):
            ty,tx = y + direction[i][1],x+direction[i][0]
            if tx in range(w) and ty in range(h) and not visited[ty][tx] and realMap[ty][tx]:
                visited[ty][tx] = True
                need_visit.append((ty,tx))



while True:
    
    count = 0

    w,h = map(int,sys.stdin.readline().rstrip().split())
    if w == h == 0 : break

    visited = [[False] * w for _ in range(h)]
    realMap = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(h)]

    for j in range(w):
        for k in range(h):
            bfs(k,j)

    answer.append(count)
    
for l in answer:
    print(l)


#따라서 해봤는데 드럽게 어렵다 이문제는 특히 여러번 해서 더어려운거같아 이런거지같으니


