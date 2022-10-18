import sys
sys.setrecursionlimit(100000)

f = sys.stdin.readline().rstrip()
s = sys.stdin.readline().rstrip()

m = len(s)
n = len(f)

dpm = [[-1]* (m+1) for _ in range(n+1)]

def lcs(f,s):
    if dpm[len(f)][len(s)] == -1:
        if len(f) == 0 or len(s) ==0:
            dpm[len(f)][len(s)] = 0
        elif f[-1] == s[-1]:
            dpm[len(f)][len(s)] = 1 + lcs(f[0:-1],s[0:-1])
        else :
            dpm[len(f)][len(s)] = max(lcs(f[0:-1],s),lcs(f,s[0:-1]))

    return dpm[len(f)][len(s)]



    # if len(f) == 0 or len(s) ==0:
    #         return 0
    # elif f[-1] == s[-1]:
    #     return 1 + lcs(f[0:-1],s[0:-1])
    # else :
    #     return max(lcs(f[0:-1],s),lcs(f,s[0:-1]))

print(lcs(f,s))


# 맞았다 이게 메모이제이션인가 dp인가?