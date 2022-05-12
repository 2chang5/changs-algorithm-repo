import itertools
import itertools

n = int(input())

ans = itertools.permutations(range(1,n+1),n)

for i in ans:
    for j in i:
        print(j,end=' ')
    print('')