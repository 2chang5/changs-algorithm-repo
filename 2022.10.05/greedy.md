https://mccoy-devloper.tistory.com/64 정리한 블로그 내용

1946번

~~~
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

    for k in reversed(people):
        people.pop()
        for l in reversed(people):
            if k[1] > l[1]:
                answer[i] -= 1
                break


for m in answer:
    print(m)
    
~~~
이거 썻을떄 시간초과남 N이 당연 100000이라 당연히 날줄알았지만 break에 희망을 걸어봤는데 고쳐봐야지

~~~
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
~~~~
이렇게 바꿧다 2중 for문 안쓰려고 해서 방법을 찾은건데 그냥 무슨 생각으로 한건지는 모르겠다 그냥 번뜩였다
아니 정렬하는거만 뺴면 당장 제일 좋은게 없자나 뭔참 문제 이런식으로 나오면 정렬해놓고 비교하는걸 한번생각하는걸 교훈으로 삼아야겠다

캔디캔디
지옥의 캔디캔디
~~~
import sys

m,n = map(int, sys.stdin.readline().rstrip().split())

greedyfriends = []

answer = 0

for _ in range(n):
    greedyfriends.append(int(sys.stdin.readline().rstrip()))

wantCandy = sum(greedyfriends)

shortCandy = wantCandy - m

realCandyDivision = greedyfriends[:]

start = 0
while shortCandy != 0:
    if realCandyDivision[start] > 0:
        realCandyDivision[start] -= 1
        shortCandy -= 1
    
    if start == n-1:
        start = 0
    else: 
        start += 1

for i in range(n):
    temp = greedyfriends[i] - realCandyDivision[i]
    answer += temp ** 2

print(answer%(2 ** 26))
~~~
시간초과남


~~~
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
~~~
그리디하게 조건에 맞도록 정렬해놓고 작은값부터 넣어준거 그리디하게 생각하는방법이긴한데 저런아이디어는 어서나오는거야 혹부리영감인가?


이분탐색으로 푼사람도 있는거같은데 이걸 왜 어떻게 이분탐색으로 푼건지 아직 이해가 안된다 좋은접근법도 아닌거같다.


1931번

~~~
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

~~~
정렬기준 하나 아닐수있다 정렬할때 기준이 겹치나 보고 그에따른 두번째 기준을 정해주던지 뭔가 해야한다.