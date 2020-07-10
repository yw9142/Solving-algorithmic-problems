import math


def solution(n, m):
    gcd_lcm = [math.gcd(n, m), n * m // math.gcd(n, m)]
    return gcd_lcm
