n = int(input())

ans = []

def vps(parenthesis):
    stack = []
   
    for i in parenthesis:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if len(stack) == 0:
                return "NO"
            elif stack[-1] == "(":
                stack.pop()

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
    

for j in range(n):
    ans.append(vps(input()))

for k in ans:
    print(k)
