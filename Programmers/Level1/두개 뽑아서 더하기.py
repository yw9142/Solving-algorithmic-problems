from itertools import combinations


def solution(numbers):
    comb = list(combinations(numbers, 2))
    lists = []

    for i in comb:
        lists.append(sum(i))

    lists = list(set(lists))
    lists.sort()

    return lists
