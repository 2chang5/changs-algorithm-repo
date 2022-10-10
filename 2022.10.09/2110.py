import sys

n,c = map(int,sys.stdin.readline().rstrip().split())

house = [int(sys.stdin.readline().rstrip()) for _ in range(n) ]

house.sort()

answer  = -1

left,right = 0 , 10**9

while left <= right:
    mid = (left+right)//2
    nowPoint = 0
    tempc = c -1
    
    for i in range(len(house)):
        if house[i] - house[nowPoint] >= mid :
            nowPoint = i
            tempc -= 1
    
    if tempc <= 0:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
            

print(answer)

# 맞았다!!!!!!