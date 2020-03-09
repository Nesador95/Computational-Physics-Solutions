# Done
import numpy as np
"""
build a code to solve n choose k problems where k >= 1
"""


def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def binomial_coefficient(n, k):
    if k == 0:
        bin_coef = 1
    else:
        bin_coef = factorial(n) / (factorial(k) * factorial(n-k))

    return int(bin_coef)

# printing Pascal's Triangle
def pascal_triangle(limit):
    for n in range(limit+1):
        line = []
        for k in range(n+1):
            line.append(binomial_coefficient(n, k))
    return line

# probability of an unbiased coin
def unbiased_coin(tosses, heads):
    probability = binomial_coefficient(tosses,heads) / 2**tosses
    return probability

print(unbiased_coin(100,60)) # 100 choose 60
for i in range(60,101): # 100 choose 60 or more
    print(unbiased_coin(100,i))
