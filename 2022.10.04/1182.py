import itertools
import sys

n,s = map(int , sys.stdin.readline().rstrip().split(" "))

numbers = list(map(int , sys.stdin.readline().rstrip().split(" ")))

answer = 0


for i in range(n):
    for j in itertools.combinations(numbers,i+1):
        if sum(j) == s :
            answer +=1 


print(answer)