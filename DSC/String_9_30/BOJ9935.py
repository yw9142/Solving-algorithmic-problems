# -*- coding:utf-8 -*-

string = input()
bomb_string = input()

string_stack = []  # 문자를 담을 Stack
check = bomb_string[-1]  # 폭발문자열의 끝 문자를 기준으로 확인
bomb_string_length = len(bomb_string)  # 확인 후에 길이 만큼 슬라이싱해서 문자열 일치 확인

for char in string:
    string_stack.append(char)

    if char == check and ''.join(string_stack[-bomb_string_length:]) == bomb_string:
        del string_stack[-bomb_string_length:]

    answer = ''.join(string_stack)

if answer == '':
    print("FRULA")
else:
    print(answer)
