def solution(n):
    num = set(range(2, n + 1))

    print(num)
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + i, i))
            print(set(range(2 * i, n + i, i)))

    return len(num)

# 참조 : https://velog.io/@joygoround/test-unsolved-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 에라토스테네스의 체
