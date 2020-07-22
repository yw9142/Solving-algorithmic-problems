# -*- encoding: utf-8 -*-


n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
dp2 = [1] * n
count = 0

for i in range(n):  # 맨 앞에서부터
    for j in range(i):
        if arr[j] < arr[i] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

for i in range(n - 1, -1, -1):  # 맨 뒤에서부터
    for j in range(n - 1, i - 1, -1):
        if arr[j] < arr[i] and dp2[i] <= dp2[j]:
            dp2[i] = dp2[j] + 1

for i in range(n):
    if count < dp[i] + dp2[i] - 1:
        count = dp[i] + dp2[i] - 1

print(count)
