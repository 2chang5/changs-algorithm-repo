def solution(s, times):
    answer = [1, -1]

    progressDate = []

    progressDate.append(list(map(int, s.split(":"))))

    for i in times:
        day, time, minute, sec = map(int, i.split(":"))
        pyear, pmonth, pday, ptime, pmintue, psec = progressDate[-1]

        calcSec = psec + sec
        if calcSec >= 60:
            minute += calcSec // 60
            conSec = calcSec % 60
        else:
            conSec = calcSec

        calcMinute = pmintue + minute
        if calcMinute >= 60:
            time += calcMinute // 60
            conMinute = calcMinute % 60
        else:
            conMinute = calcMinute

        calcTime = ptime + time
        if calcTime >= 24:
            day += calcTime // 24
            conTime = calcTime % 24
        else:
            conTime = calcTime

        calcDay = pday + day
        if calcDay > 30:
            pmonth += calcDay // 30
            conDay = calcDay % 30
        else:
            conDay = calcDay

        if pmonth > 12:
            pyear += pmonth // 12
            conMonth = pmonth % 12
        else:
            conMonth = pmonth

        conYear = pyear

        conclusion = [conYear, conMonth, conDay, conTime, conMinute, conSec]

        progressDate.append(conclusion)

    answer[1] = (progressDate[-1][0] - progressDate[0][0]) * 360 + (progressDate[-1][1] - progressDate[0][1]) * 30 + (
            progressDate[-1][2] - progressDate[0][2] + 1)

    for i in range(len(progressDate) - 1):
        if progressDate[i][1] != 12:
            if progressDate[i][0] != progressDate[i + 1][0]:
                answer[0] = 0
                break
        if progressDate[i][2] != 30:
            if progressDate[i][1] != progressDate[i + 1][1]:
                answer[0] = 0
                break
            if progressDate[i + 1][2] - progressDate[i][2] != 1:
                answer[0] = 0
                break
        else:
            if progressDate[i + 1][2] != 0:
                answer[0] = 0
                break

    return answer
