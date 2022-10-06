import sys

m,n = map(int, sys.stdin.readline().rstrip().split())

greedyfriends = []

answer = 0

for _ in range(n):
    greedyfriends.append(int(sys.stdin.readline().rstrip()))

wantCandy = sum(greedyfriends)

shortCandy = wantCandy - m #부족분

#그리디 하게 풀어볼려면 -> 정렬 + 부족분 분배가 원하는 사탕을 넘을수없다는거 그중에서 그냥 쭉쭉 줘나가는게 포인드
greedyfriends.sort()

for i in range(n):
    temp = min(shortCandy//(n-i),greedyfriends[i])
    answer += temp ** 2
    shortCandy -= temp
    

print(answer%(2 ** 64))