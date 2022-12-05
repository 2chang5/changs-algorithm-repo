import sys
from collections import deque

sys.stdin.readline().rstrip()

A = list(sys.stdin.readline().rstrip().split())

sys.stdin.readline().rstrip()

M = list(sys.stdin.readline().rstrip().split())

answer = []
A.sort()
A = deque(A)

processedM = []

for i in range(len(M)):
    processedM.append((i, M[i]))

processedM.sort(key=lambda x: x[1])
processedM = deque(processedM)

while processedM:
    if A:
        if A[0] == processedM[0][1]:
            if len(processedM) > 1:
                if processedM[1][1] == processedM[0][1]:
                    answer.append((processedM.popleft()[0], 1))
                else:
                    A.popleft()
                    answer.append((processedM.popleft()[0], 1))
            else:
                A.popleft()
                answer.append((processedM.popleft()[0], 1))
            continue
        if A[0] > processedM[0][1]:
            answer.append((processedM.popleft()[0], 0))
            continue
        if A[0] < processedM[0][1]:
            A.popleft()
            continue
    else:
        answer.append((processedM.popleft()[0], 0))

answer.sort(key=lambda x: x[0])

for i in answer:
    print(i[1])
