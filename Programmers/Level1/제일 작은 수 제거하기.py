def solution(arr):
    if len(arr) == 1:
        arr.pop()
        arr.append(-1)
        return arr

    minimum = min(arr)
    arr.remove(minimum)
    return arr
