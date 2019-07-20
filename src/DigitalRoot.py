# Sum of Digits / Digital Root
# https://www.codewars.com/kata/541c8630095125aba6000c00/


def digital_root(n):
    sum_of_digits = sum(map(int, str(n)))
    if sum_of_digits in range(10):
        return n
    else:
        digital_root(sum_of_digits)
