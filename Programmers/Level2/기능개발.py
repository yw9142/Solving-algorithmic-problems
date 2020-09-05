from math import ceil


def solution(progresses, speeds):
    days = []
    answer = []

    for i in range(len(progresses)):  # 7 70 45
        days.append(ceil((100 - progresses[i]) / speeds[i]))

    count = 0
    while days:
        if count == 0:
            target = days.pop(0)
            count += 1
            continue

        if target >= days[0]:
            days.pop(0)
            count += 1
        else:
            answer.append(count)
            count = 0

    answer.append(count)

    return answer
