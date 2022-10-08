import sys

n = int(sys.stdin.readline().rstrip())

temp = 1000 - n

answer = 0

coin = [500,100,50,10,5,1]

for i in coin:
    answer += temp // i
    temp %= i

print(answer)