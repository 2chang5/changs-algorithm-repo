def solution(flowers):
    answerSet = set()

    for i in flowers:
        for j in range(i[0],i[1]):
            answerSet.add(j)

    answer = len(answerSet)
    return answer