# -*- encoding: utf-8 -*-
# fibonacci

def fibonacci(N1, N2, N):
    while N > 1:
        N1, N2 = N2, N1 + N2
        N -= 1

    return N1, N2


def solution(N):
    N1 = 1  # N-1번째 사각형 변의 길이
    N2 = 1  # N번째 사각형 변의 길이

    N1, N2 = fibonacci(N1, N2, N)  # fibonacci 함수를 통해 N-1번째 변의 길이, N번째 변의 길이를 얻어옴

    answer = (N1 + N2) * 2  # (N1 + N2) * 2 = 둘레의 길이
    return answer
