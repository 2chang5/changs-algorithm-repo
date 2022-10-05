import sys

n = int(sys.stdin.readline().rstrip())

dice = []

answer = 0

for i in range(n):
   dice.append(list(map(int, sys.stdin.readline().rstrip().split(" ")))) 

for j in range(n):
    if dice[0] == 6 :
        answer += 5
    else: 
        answer += 6


print(answer)


# 주사위 왜 5랑 6만 더해주면 될꺼같은데 그리고 애초에 예시는 다 6이면되는거아냐?
# 이거 상의해봐야겠다


#아 문제 다시보고 이해함 예전 풀이대로 풀면될듯