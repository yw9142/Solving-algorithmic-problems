def solution(s):
    bracket = []
    for i in s:
        if i == '(':
            bracket.append(i)
        else:
            if len(bracket) == 0:
                return False
            else:
                bracket.pop()

    if len(bracket) == 0:
        return True
    else:
        return False
