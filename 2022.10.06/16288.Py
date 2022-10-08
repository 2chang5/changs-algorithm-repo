#생각하다가 머리 아파서 답지보고 이해하긴했는데 아니 이런것도 그디네 그냥 정렬하면 다 그리디인가 얼탱이없다
from operator import index
import sys

n,k = map(int, sys.stdin.readline().rstrip().split())

orderList = list(map(int,sys.stdin.readline().rstrip().split()))

lines = [[0] for _ in range(k)]

answer = "YES"

for i in orderList:
    for j in lines:
        if j[-1] < i:
            j.append(i)
            break
            
        if lines.index(j) == k-1:
            answer = "NO"


print(answer)

#사실 배열들로 구현할필요없이 마지막 숫자들만 기억한 리스트면 되는데 그냥 배열 구현 해볼라고 이중배열로 했다