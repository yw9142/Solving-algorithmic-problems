def solution(numbers, target):
    cases = [0]

    for i in numbers:
        new_cases = []
        for j in cases:
            new_cases.append(j + i)
            new_cases.append(j - i)
        cases = new_cases
    return cases.count(target)
