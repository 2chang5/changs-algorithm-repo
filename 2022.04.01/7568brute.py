n = int(input())
people = []
ranking = [1 for i in range(n)]

for i in range(n):
    people.append(input().split())

for i in range(n):
    people[i][0]=int(people[i][0])
    people[i][1]=int(people[i][1])

for i in range(n):
    for j in people:
       if people[i][0] < j[0] and people[i][1] < j[1]:
           ranking[i] = ranking[i]+1 

for i  in ranking:
    print(i, end = " ")

