from ast import And
import sys

n = int(sys.stdin.readline().rstrip())
people = []

answer = [ 1 for _ in range(n)]

for i in range(n):
    people.append(list(map(int,sys.stdin.readline().rstrip().split(" "))))

for j in range(len(people)):
    for k in people:
        if j == people.index(k) :
            pass
        else:
            if people[j][0] < k[0] and people[j][1] < k[1]:
                answer[j] += 1

for m in answer:
    print(m,end= " ")