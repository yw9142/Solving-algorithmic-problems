def solution(prices):
    answer = [0] * len(prices)  # price의 개수만큼 생성

    for i in range(len(prices) - 1):  # 0 ~ len(price)
        for j in range(i, len(prices) - 1):  # i ~ len(price)
            if prices[i] > prices[j]:  # 감소했으면 탈출
                break
            else:  # 증가추세면 day += 1
                answer[i] += 1

    return answer
