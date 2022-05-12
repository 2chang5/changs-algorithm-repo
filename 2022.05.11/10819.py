import itertools

ans = 0

n = int(input())

nums = list(map(int,input().split()))

per = itertools.permutations(nums,len(nums))

for i in per:
    tempans = 0
    for j in range(n-1):
        tempans = tempans + abs(i[j]-i[j+1])
    if ans < tempans :
        ans = tempans 

print(ans)