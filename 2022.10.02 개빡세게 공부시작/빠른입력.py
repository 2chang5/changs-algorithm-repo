from itertools import combinations_with_replacement

sets = [1,2,3]

data = combinations_with_replacement(sets, 2)

for i in data:
   print(i)