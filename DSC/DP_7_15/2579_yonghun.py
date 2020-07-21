# -*- encoding: utf-8 -*-


number = int(input())

stair = [0] * 301  # 최대 300개
dp = [0] * 301

for i in range(number):
    stair[i] = int(input())

# 0 1 2 3 4 5 6 7 8 --------
dp[0] = stair[0]  # stair[0]은 1번째 계단을 오르는 경우만 존재
dp[1] = max(stair[0] + stair[1], stair[1])  # 0, 1 연속으로 가는 방법 OR 1로 한번에 가는 방법
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])  # 1 / 2  OR 2 / 1 두 가지 방법

for i in range(3, number):
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])  # 표를 확인

print(dp[number - 1]) # 맨 마지막이 결과값
