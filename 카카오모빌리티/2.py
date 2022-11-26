def solution(id_list, k):
    answer = 0

    customerDict = {}

    for i in id_list:
        for j in i.split():
            customerDict[j] = 0

    for i in id_list:
        for j in customerDict.keys():
            if j in i:
                customerDict[j] += 1

    for i in customerDict.values():
        if i > k:
            answer += k
        else:
            answer += i

    return answer
