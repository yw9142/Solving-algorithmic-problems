def solution(n):
    next_number = n + 1

    while True:
        if bin(next_number).count('1') == bin(n).count('1'):
            return next_number
        next_number += 1
