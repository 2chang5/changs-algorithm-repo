import sys

n = int(sys.stdin.readline().rstrip())

chemical = list(map(int,(sys.stdin.readline().rstrip().split())))

chemical.sort()

start = chemical[0]+chemical[-1]
temp = [chemical[0],chemical[-1]]

if n % 2 == 0 :
    for i in range(0,n/2+1):
        if abs(start) > abs(chemical[i]+ chemical[(i*-1)-1]):
            temp[0]= chemical[i]
            temp[-1] = chemical[(i*-1)-1]
else:
    for i in range(0,n//2):
        if abs(start) > abs(chemical[i]+ chemical[(i*-1)-1]):
            temp[0]= chemical[i]
            temp[-1] = chemical[(i*-1)-1]
    if abs(start) > abs(chemical[n//2]+chemical[n//2+1]):
        temp[0]= chemical[n//2]
        temp[-1] = chemical[n//2+1]
    if abs(start) > abs(chemical[n//2+1]+chemical[n//2+2]):
        temp[0]= chemical[n//2+1]
        temp[-1] = chemical[n//2+2]

print(temp[0],temp[1])