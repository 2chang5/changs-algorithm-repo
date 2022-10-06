import sys

n,k = map(int,sys.stdin.readline().rstrip().split())

coin_type = []

answer = 0

for i in range(n):
    coin_type.append(int(sys.stdin.readline().rstrip()))

coin_type.sort(reverse=True)

for i in coin_type:
    answer += k//i
    k %= i

print(answer)