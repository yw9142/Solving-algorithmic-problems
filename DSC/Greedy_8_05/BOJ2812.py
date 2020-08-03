# -*- encoding: utf-8 -*-
import sys

input = sys.stdin.readline

N, K = map(int, input().split())  # 4 2
number = list(input().strip())  # 1 9 2 4

list_number = []
new_K = K

for i in range(N):
    # new_K가 0이상 and list_number가 안비어있다 and list_number의 끝부분이 number[i]보다 작을때
    while new_K > 0 and list_number and list_number[-1] < number[i]:
        del list_number[-1]  # list_number의 끝부분을 지우고
        new_K -= 1  # new_K 하나 감소

    list_number.append(number[i])  # 다시 list_number에 number[i]를 추가
print(''.join(list_number[:N - K]))

#         number    list_number
# ex)N=1 1 9 2 4 / -> 1 9 2 4 / 1
# ex)N=2 1 9 2 4 / 9 -> 9 2 4 / 9
# ex)N=3 1 9 2 4 / 9 -> 2 4 / 9 2
# ex)N=4 1 9 2 4 / 9 2 -> 4 / 9
# ex)N=4 1 9 2 4 / 9 -> 4 / 9 4

# for i in range(K):
#     list_number.remove(min(list_number))
#
# essence = ''.join(map(str, list_number))
# print(int(essence))
