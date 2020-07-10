def solution(arr1, arr2):
    temp = []
    new_array = []

    for a, b in zip(arr1, arr2):
        for c, d in zip(a, b):
            temp.append(c + d)
        new_array.append(temp)
        temp = []
    return new_array
