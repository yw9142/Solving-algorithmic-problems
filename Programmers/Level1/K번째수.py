def solution(array, commands):
    answer_array = []
    for num in commands:
        i, j, k = num[0], num[1], num[2]
        new_array = array[i - 1:j]
        new_array.sort()
        answer_array.append(new_array[k - 1])
    return answer_array
