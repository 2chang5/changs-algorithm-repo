def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))

    answer = []

    # 첫번쨰 인천으로 고정하기
    for i in tickets:
        if i[0] == "ICN":
            answer.extend(i)
            tickets.remove(i)
            break

    while tickets:
        for i in tickets:
            if answer[-1] == i[0]:
                answer.append(i[1])
                tickets.remove(i)
                break

    return answer


