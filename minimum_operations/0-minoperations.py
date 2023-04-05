#!/usr/bin/python3
"""
Minimum operators - module
"""


import math


def minOperations(n):
    """Minimum operators - function"""
    if not isinstance(n, int) or n <= 0:
        return 0

    factors = []
    while n % 2 == 0:
        factors.append(2)
        print(factors)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        print("soy el ciclo for")
        while n % i == 0:
            factors.append(i)
            print(factors)
            n //= i

    if n > 2:
        factors.append(n)

    return sum(factors)
