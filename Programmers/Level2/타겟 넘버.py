def solution(numbers, target):
    cases = [0]

    for i in numbers:
        new_cases = []
        for j in cases:
            new_cases.append(j + i)
            new_cases.append(j - i)
        cases = new_cases
    return cases.count(target)

# ex)
# [1, -1]
# [2, 0, 0, -2]
# [3, 1, 1, -1, 1, -1, -1, -3]
# [4, 2, 2, 0, 2, 0, 0, -2, 2, 0, 0, -2, 0, -2, -2, -4]
# [5, 3, 3, 1, 3, 1, 1, -1, 3, 1, 1, -1, 1, -1, -1, -3, 3, 1, 1, -1, 1, -1, -1, -3, 1, -1, -1, -3, -1, -3, -3, -5]

# len(number)
# 가능한 경우의 수의 개수는 2^len(number)
# 위의 예시의 경우 5개이므로 2^5 = 32개의 경우의 수가 존재하고 그 중 3인 경우만을 추출한 것임.
