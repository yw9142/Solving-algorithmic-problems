# -*- encoding: utf-8 -*-


def palindrome(index, length, str):  # Palindrome 확인 함수
    i = 0
    while index + i < length - i - 1:
        if str[index + i] != str[length - i - 1]:  # palindrome은 i == N - i - 1 이면 성립함.
            return False  # 하나라도 성립하지 않는다면 return False
        i += 1
    return True  # 모두 성립한다면 return True


if __name__ == '__main__':
    str = input()  # 문자열 입력받기
    length = len(str)  # 문자열의 길이
    answer = 0  # Palindrome의 길이

    for i in range(length):  # length / length + 1 / length + 2
        if palindrome(i, length, str):
            answer = length + i
            break

    print(answer)

# Manacher's algorithm :
# https://algospot.com/wiki/read/Manacher's_algorithm
# http://www.secmem.org/blog/2019/03/10/Manacher/
