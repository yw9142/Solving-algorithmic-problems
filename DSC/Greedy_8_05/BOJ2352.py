import bisect
import sys

input = sys.stdin.readline

n = int(int(input()))
port_number = list(map(int, input().split()))

new_port_number = [port_number[0]]

for i in range(1, n):
    if new_port_number[-1] < port_number[i]:
        new_port_number.append(port_number[i])
    else:
        new_port_number[bisect.bisect_left(new_port_number, port_number[i])] = port_number[i]

print(len(new_port_number))
