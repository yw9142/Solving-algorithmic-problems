def solution(x, n):
    new_array = []
    for i in range(1, n + 1):
        new_array.append(x * i)

    return new_array
