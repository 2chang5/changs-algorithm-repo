import sys

sys.stdin.readline().rstrip()
first, second = map(list, sys.stdin.readline().rstrip().split(" "))

if len(first) > len(second):
    bigger = first
    smaller = second
else:
    bigger = second
    smaller = first

combineName = ""

for i in range(len(smaller)):
    combineName += (first.pop(0) + second.pop(0))

combineName += "".join(bigger)

processedCombineName = list(combineName)
combineNameCount = []

alphabet = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
count = 3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1

countDict = dict(zip(alphabet, count))

for i in processedCombineName:
    combineNameCount.append(countDict[i])

while len(combineNameCount) > 2:
    tempCombineNameCount = []
    for i in range(0, len(combineNameCount) - 1):
        tempCombineNameCount.append((combineNameCount[i] + combineNameCount[i + 1]) % 10)
    combineNameCount = tempCombineNameCount

print(str(int("".join(map(str, combineNameCount)))) + "%")
