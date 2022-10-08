import sys 

n = int(sys.stdin.readline().rstrip())

meetingList = []

for _ in range(n):
    meetingList.append(list(map(int,sys.stdin.readline().rstrip().split())))

meetingList.sort(key= lambda x : (x[1], x[0]))

answer = 1

start = meetingList[0]

del(meetingList[0])

for i in meetingList:
    if start[1] <= i[0]:
        answer += 1
        start = i
        

print(answer)

