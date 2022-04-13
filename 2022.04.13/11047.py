n,k = map(int,input().split())

coin = []

ans = 0

for i in range(n):
    coin.append(int(input()))


coin.sort(reverse=True)

for j in coin:
    if j <= k:
        while not(k - j < 0): 
            k = k - j
            ans = ans + 1

        
print(ans)