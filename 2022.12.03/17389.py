import sys

sys.stdin.readline().rstrip()

oxCon = list(sys.stdin.readline().rstrip())



con = 0

bonus = 0

for i in range(len(oxCon)):
    if oxCon[i] == "O":
        con += i+1
        con += bonus
        bonus += 1
    else:
        bonus = 0

print(con)
