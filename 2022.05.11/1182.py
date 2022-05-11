import itertools
ans = 0

n,s = map(int,input().split())

nums = list(map(int,input().split()))

for i in range(1,6):
    for j in itertools.combinations(nums,i):
        if sum(j) == s:
            ans += 1
    
print(ans)