import itertools

n = int(input())

for i in itertools.permutations(range(1,n+1),n):
    print(i)