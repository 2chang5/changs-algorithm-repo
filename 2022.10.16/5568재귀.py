import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

card = [int(sys.stdin.readline().rstrip()) for _ in range(n)]


#permutation 으로 푼다
# import itertools

# allCard = list(itertools.permutations(card,k))

# answerSet = set()

# for i in allCard:
#     temp = str()
#     for j in i:
#         temp += str(j)
#     answerSet.add(temp)   

# print(len(answerSet))


#재귀로 푼다
