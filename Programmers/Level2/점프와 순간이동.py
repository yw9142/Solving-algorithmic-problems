def solution(n):
    answer = 0
    while n > 0:  # 1, 2, 4, 8, 16, 32 -------
        n, b = divmod(n, 2)
        answer += b
    return answer
