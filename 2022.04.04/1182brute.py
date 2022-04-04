from itertools import combinations

n,s = map(int,input().split())

arr = list(map(int,input().split()))

con = 0

for i in range(n):
    for j in combinations(arr,i+1):
        if sum(j) == s:
            con += 1


print(con)