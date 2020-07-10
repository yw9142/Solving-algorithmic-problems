def solution(arr, divisor):
    possible_divide = []
    for i in arr:
        if i % divisor == 0:
            possible_divide.append(i)

    if len(possible_divide) == 0:
        possible_divide.append(-1)
        return possible_divide
    else:
        possible_divide.sort()
        return possible_divide
