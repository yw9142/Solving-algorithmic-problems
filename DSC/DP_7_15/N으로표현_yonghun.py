# -*- encoding: utf-8 -*-


def solution(N, number):
    number_set = [set() for _ in range(8)]

    for i, x in enumerate(number_set, start=1):
        print(i)
        print(x)
        x.add(int(str(N) * i))  # set이기 때문에 append가 아닌 add를 넣어줘야함

    for i in range(1, 8):  # 대환장 4중 for문 우리 알고리즘 선생님 보면 우실 듯
        for j in range(i):  # 사실 왜 7까지만 도는지 이해 못함 2+7이 9가 돼서 그런건가봄
            for op1 in number_set[j]:
                for op2 in number_set[i - j - 1]:
                    number_set[i].add(op1 + op2)
                    number_set[i].add(op1 - op2)
                    number_set[i].add(op1 * op2)
                    if op2 != 0 and op1 % op2 == 0:
                        number_set[i].add(op1 // op2)
        if number in number_set[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer

print(solution(5, 12))