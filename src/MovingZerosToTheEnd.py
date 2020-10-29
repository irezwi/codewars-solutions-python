# Moving Zeros To The End
# https://www.codewars.com/kata/52597aa56021e91c93000cb0


from itertools import compress


def move_zeros(array):
    non_zero = list(compress(array, map(lambda x: x != 0 or x is False, array)))
    zeroes = [0] * (len(array) - len(non_zero))
    return non_zero + zeroes
