import sys

m,n = map(int, sys.stdin.readline().rstrip().split())

greedyFriends = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

answer = 0

greedyFriends.sort()

shortCandy = sum(greedyFriends) - m

left,right = 0 , 2*10**9

temp = -1

while left <= right:
    mid = (left+right) // 2
    divdedShortCandy = 0

    for i in greedyFriends:
        divdedShortCandy += min (mid,i)

    if divdedShortCandy <= shortCandy:
        temp = mid
        left = mid + 1
    else :
        right = mid -1

gavedcandy = 0

for j in greedyFriends:
    gavedcandy += min(temp,j)

notGavedCandy = shortCandy - gavedcandy

for j in greedyFriends:
    # tempCandy = min(j, temp+1 if notGavedCandy > 0 else temp) 
    tempCandy = min(j,temp)
    if j > temp :
        if notGavedCandy > 0 :
            tempCandy += 1
    answer += tempCandy ** 2
    shortCandy -= tempCandy 

    if shortCandy == 0 :
        break
    
    if notGavedCandy > 0:
        notGavedCandy -= 1
    
print(answer%(2 ** 64))

# 이진탐색으로 안풀어 죄다 틀리네 안해 