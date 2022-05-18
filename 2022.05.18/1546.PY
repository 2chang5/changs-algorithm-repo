n = int(input())

arr = list(map(int,input().split()))

bigest = max(arr)
total = 0

def everage(now):
    global bigest
    global total
    total += now/bigest*100
    
for i in arr:
    everage(i)

print(total/n)