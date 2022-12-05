import sys
from collections import deque

n, name = sys.stdin.readline().rstrip().split(" ")

carmel = ""
snake = ""
pascal = ""

if n == "1":
    carmel = name
    pascalDeque = deque(name)
    pascalDeque.appendleft(pascalDeque.popleft().upper())
    pascal = "".join(pascalDeque)
    snakeDeque = deque()
    for i in reversed(list(name)):
        if i.isupper():
            snakeDeque.appendleft(i.lower())
            snakeDeque.appendleft("_")
        else:
            snakeDeque.appendleft(i)
    snake = "".join(snakeDeque)

if n == "2":
    snake = name
    carmelList = list(name)
    processedCarmelList = []
    for i in range(len(carmelList)):
        if carmelList[i] == "_":
            carmelList[i + 1] = carmelList[i + 1].upper()
        else:
            processedCarmelList.append(carmelList[i])
    carmel = "".join(processedCarmelList)
    pascalDeque = deque(carmel)
    pascalDeque.appendleft(pascalDeque.popleft().upper())
    pascal = "".join(pascalDeque)

if n == "3":
    pascal = name
    carmelDeque = deque(name)
    carmelDeque.appendleft(carmelDeque.popleft().lower())
    carmel = "".join(carmelDeque)
    snakeDeque = deque()
    for i in carmel:
        if i.isupper():
            snakeDeque.append("_")
            snakeDeque.append(i.lower())
        else:
            snakeDeque.append(i)

    snake = "".join(snakeDeque)

print(carmel)
print(snake)
print(pascal)
