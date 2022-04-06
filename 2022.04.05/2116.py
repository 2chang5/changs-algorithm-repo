import copy

n = int(input())
dicelist = []

tempconclusion = 0
conclusion = 0

for i in range(n):
    dicelist.append(list(map(int,input().split())))


def anotherSide(number):
    if number == 0:
        return 5
    elif number == 1:
        return 3
    elif number == 2:
        return 4
    elif number == 3:
        return 1    
    elif number == 4:
        return 2
    elif number == 5:
        return 0

for i in dicelist[0]:
    up =i
    tempDiceList = []
    for k in dicelist:
        tempDiceList.append(k[:])
    for j in range(n):
        down = dicelist[j][anotherSide(dicelist[j].index(up))]
        tempDiceList[j].remove(up)
        tempDiceList[j].remove(down)
        tempconclusion += max(tempDiceList[j])
        up = down
    if conclusion < tempconclusion:
        conclusion = tempconclusion
    tempconclusion = 0

print(conclusion)