import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

conclusion ={'R': 0 ,'G': 0 ,'B':0, 'be': 0 }

direction = [(-1,0),(0,-1),(0,1),(1,0)]


def bfs(y,x,color):
    
    global visited,queue,conclusion

    if color == 'be':

        if graph[y][x] == 'B' or visited[y][x] : return
    
        conclusion[color] += 1

        queue.append((y,x))

        while queue:

            ty,tx = queue.popleft()

            for i in range(4):
                tty,ttx = ty+direction[i][0],tx+direction[i][1]
                if tty in range(n) and ttx in range(n) and not visited[tty][ttx]:
                    if graph[tty][ttx] == 'R' or graph[tty][ttx] == 'G':
                        visited[tty][ttx] = True
                        queue.append((tty,ttx))
    else :
        
        if graph[y][x] != color or visited[y][x] : return
    
        conclusion[color] += 1

        queue.append((y,x))
        
        while queue :
            ty,tx = queue.popleft()

            for i in range(4):
                tty,ttx = ty+direction[i][0],tx+direction[i][1]
                if tty in range(n) and ttx in range(n) and not visited[tty][ttx] and graph[tty][ttx] == color:
                    visited[tty][ttx] = True
                    queue.append((tty,ttx))
   


for i in conclusion.keys() :

    visited = [[False] * n for _ in range(n)]
    
    queue = deque()

    for w in range(n):
        for h in range(n):
            bfs(h,w,i)


print(conclusion['R']+conclusion['G']+conclusion['B'],conclusion['B']+conclusion['be'])
    

