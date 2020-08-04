def solution(number, k):
    number = list(number)
    list_number = []
    temp = k

    for i in range(len(number)):
        while temp > 0 and list_number and list_number[-1] < number[i]:
            del list_number[-1]
            temp -= 1
        list_number.append(number[i])

    return ''.join(list_number[:len(number) - k])
