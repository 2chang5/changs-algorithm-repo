import sys 

input = sys.stdin.readline

T = int(input().rstrip())

answer = []

for i in range(T):
    n = int(input().rstrip())
    answer.append(n)
    people = []
    for j in range(n):
        people.append(list(map(int, input().rstrip().split())))
    
    people.sort(key = lambda x: x[0])

    temp = people[0]
    
    del(people[0])
  
    for k in people:
        if temp[1] > k[1]:
            temp = k
        else:
            answer[i] -= 1


for m in answer:
    print(m)