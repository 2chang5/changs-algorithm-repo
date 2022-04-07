from itertools import combinations

l,c = map(int,input().split())

ja = []
mo = []
con = []

raw = input().split()


for i in raw:
    if i == 'a' or i == 'e' or i =='i' or i == 'o' or i =='u':
        mo.append(i)
    else : 
        ja.append(i)


for j in mo:
    tempmo = mo[:]
    tempmo.remove(j)
    rest = []
    rest.extend(tempmo)
    rest.extend(ja)
    for k in combinations(rest,l-1):
        tempcon = []
        tempcon.append(j)
        tempcon.extend(k)
        if len(set(tempcon)&set(ja)) < 2:
            continue
        tempcon.sort()
        con.append(''.join(tempcon))



for i in sorted(list(set(con))):
    print(i)


