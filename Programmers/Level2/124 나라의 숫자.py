def solution(n):
    answer = ""
    while n > 0:
        remainder = n % 3
        answer = "412"[n % 3] + answer
        n //= 3
        if remainder == 0:
            n -= 1

    return answer

## 바꾸는 방법 3진법으로써 "몫 + 나머지가 0일경우 4" ##
## 6은 14 7은 21? -1?
# 4 == 11
