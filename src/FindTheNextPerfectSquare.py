# Find the next perfect square!
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013

from math import sqrt


def find_next_square(sq):
    if sqrt(sq) % 1:
        return -1
    return (sqrt(sq) + 1) ** 2
