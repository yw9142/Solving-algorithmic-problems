def solution(n):
    first, second = 0, 1
    
    for i in range(1, n):
        first, second = second, first + second
    
    return second % 1234567
    
