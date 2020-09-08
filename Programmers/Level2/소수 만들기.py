from itertools import combinations

n = 10000

A = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if A[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            A[j] = False


def Eratosthenes(first_num, second_num, third_num):  # 소수를 판별하는 에라토스테네스의 체
    total = first_num + second_num + third_num
    return A[total]


def solution(nums):
    answer = 0

    possible = list(combinations(nums, 3))  # 이 문제를 풀어내는 핵심적인 함수는 합의 경우의 수를 모두 리턴해주는 combinations 함수이다.
    for value in possible:
        if Eratosthenes(value[0], value[1], value[2]):
            answer += 1
    return answer
