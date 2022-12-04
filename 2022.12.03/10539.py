import sys

sys.stdin.readline().rstrip()

carzySubin = list(map(int, sys.stdin.readline().rstrip().split(" ")))

answer = [carzySubin[0]]
for i in range(len(carzySubin)):
    carzySubin[i] *= i + 1

for i in range(len(carzySubin) - 1):
    answer.append(carzySubin[i + 1] - carzySubin[i])

for i in answer:
    print(i, end=" ")
