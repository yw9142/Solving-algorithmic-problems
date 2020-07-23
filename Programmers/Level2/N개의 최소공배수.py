from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)


def solution(arr):
    new_lcm = 1
    
    for i in arr:
        new_lcm = lcm(new_lcm, i)
    return new_lcm
    
