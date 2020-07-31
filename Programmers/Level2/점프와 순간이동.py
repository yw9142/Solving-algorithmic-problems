def solution(n):
    answer = 0
    while n > 0:  # 1, 2, 4, 8, 16, 32 -------
        n, b = divmod(n, 2)
        answer += b
    return answer

# 다른 풀이
# def solution(n):
#     return bin(n).count('1')
# 언제나 이진수로 푸는 것을 보는건 신기하다. 이런 생각을 하는 것이 대단하다.
