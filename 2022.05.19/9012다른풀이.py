n = int(input())

ans = []

def vps(parenthesis):
    stack = 0
   
    for i in parenthesis:
        if i == "(":
            stack += 1
        elif i == ")":
            if stack <= 0:
                return "NO"
            else:
                stack -= 1

    if stack == 0:
        return "YES"
    else:
        return "NO"
    

for j in range(n):
    ans.append(vps(input()))

for k in ans:
    print(k)