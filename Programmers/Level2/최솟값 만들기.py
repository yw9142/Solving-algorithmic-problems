def solution(A,B):
    answer = 0
    A = sorted(A) # 1 2 4
    B = sorted(B, reverse=True) # 5 4 4

    new_answer = []
    for a, b in zip(A, B):
        new_answer.append(a * b)

    answer = sum(new_answer)
    return answer
