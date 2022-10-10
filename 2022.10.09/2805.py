import sys

n,m = map(int,sys.stdin.readline().rstrip().split())

trees = list(map(int,sys.stdin.readline().rstrip().split()))

left,right = 0,10**10

answer = -1

while left <= right:
    mid = (left + right) // 2
    greed = 0

    for i in trees:
        if i > mid :
            greed += i - mid

    if greed >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)