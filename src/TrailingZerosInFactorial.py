# Number of trailing zeros of N!
# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/

from math import floor, log


def zeros(n):
    if n == 0:
        return 0
    k_max = int(floor(log(n, 5)))
    z = 0
    for k in range(1, k_max + 1):
        z += floor(n / 5 ** k)
    return z
