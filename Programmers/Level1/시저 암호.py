def solution(s, n):
    new_string = []
    for i in s:
        if i.isalpha():  # 알파벳인지 확인부터
            if 65 <= ord(i) <= 90:  # 대문자 알파벳
                if ord(i) + n > 90:  # 더했는데 Z를 넘으면
                    new_string.append(chr(ord(i) - 26 + n))
                else:  # 더해도 Z를 넘지 않으면
                    new_string.append(chr(ord(i) + n))
            else:  # 소문자 알파벳
                if ord(i) + n > 122:  # 더했는데 z를 넘으면
                    new_string.append(chr(ord(i) - 26 + n))
                else:  # 더해도 z를 넘지 않으면
                    new_string.append(chr(ord(i) + n))
        else:  # 알파벳이 아니면 append 공백
            new_string.append(' ')
    return ''.join(new_string)
