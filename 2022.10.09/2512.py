import sys

n =int(sys.stdin.readline().rstrip())

budget = list(map(int,sys.stdin.readline().rstrip().split()))

total = int(sys.stdin.readline().rstrip())

S = sum(budget)
if total >= S:
    print(max(budget))
    exit()


budget.sort()

left,right = 0, 10**10

temp = -1

while left <= right:
    mid =(left + right)//2
    tempTotal = 0

    for i in budget:
        tempTotal += min(mid,i)

    if tempTotal <= total:
        temp = mid 
        left = mid + 1
    else:
        right = mid - 1


print(temp)



