import sys

sys.stdin.readline().rstrip()

scores = list(map(int, sys.stdin.readline().rstrip().split(" ")))

print(max(scores) - min(scores))
