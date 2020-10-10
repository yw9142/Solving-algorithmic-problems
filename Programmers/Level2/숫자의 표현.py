def solution(n):  # 15
    count = 0
    for i in range(1, n + 1):  # 1 ~ 15
        num = 0
        for j in range(i, n + 1):  # 1 / 2 / 3 / 4 .. ... .. ..  ~ 15
            num += j
            if num == n:
                count += 1
                break
            if num > n:
                break
    return count

# 참고 : https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-%EC%88%AB%EC%9E%90%EC%9D%98-%ED%91%9C%ED%98%84
