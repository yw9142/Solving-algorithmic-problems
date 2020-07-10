from operator import itemgetter

def solution(strings, n):
    return sorted(sorted(strings), key = itemgetter(n))

# 참고 : https://ychae-leah.tistory.com/42
