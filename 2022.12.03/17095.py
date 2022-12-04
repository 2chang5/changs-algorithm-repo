import sys

sys.stdin.readline().rstrip()

nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))

maxNum = max(nums)
minNum = min(nums)

latestMax = nums.index(maxNum)
latestMin = nums.index(minNum)

length = abs(latestMax - latestMin) + 1

for i in range(len(nums)):
    if nums[i] == maxNum:
        tempCalc = abs(latestMin - i) + 1
        if tempCalc < length:
            length = tempCalc
        latestMax = i
    elif nums[i] == minNum:
        tempCalc = abs(latestMax - i) + 1
        if tempCalc < length:
            length = tempCalc
        latestMin = i

if maxNum == minNum:
    print(1)
else:
    print(length)
