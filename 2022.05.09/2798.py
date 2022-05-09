import itertools

n,m = map(int,input().split(" "))

arr = map(int,input().split(" "))

ans = 0

for i in itertools.combinations(arr,3):
    if ans < sum(i) <= m:  
        ans = sum(i)

print(ans)

