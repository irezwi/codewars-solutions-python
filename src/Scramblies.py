# Scramblies
# https://www.codewars.com/kata/55c04b4cc56a697bb0000048

from collections import Counter


def scramble(s1, s2):
    word = Counter(s1)
    word.subtract(s2)
    return not any(v < 0 for v in word.values())
