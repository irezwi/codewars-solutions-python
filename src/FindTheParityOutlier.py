# Find The Parity Outlier
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc


def find_outlier(integers):
    even_counter, odd_counter = 0, 0
    for number in integers:
        if number % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1

    # Checks if outlier is odd or even number
    if odd_counter > 1:
        for number in integers:
            if number % 2 == 0:
                return number
    else:
        for number in integers:
            if number % 2 == 1:
                return number
