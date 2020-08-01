def solution(s):
    s = list(reversed(list(s)))
    stack = [s.pop()]
    while s:
        check = s.pop()
        if len(stack) == 0 or stack[-1] != check:
            stack.append(check)
        else:
            stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0


# a a b a a b
# stack = b
# check = a
# 간단하게 지금 문자와 그 뒤의 문자랑 비교를 해서 같으면 pop해주는 식으로 풀 수 있었는듯
