# Catching Car Mileage Numbers
# https://www.codewars.com/kata/52c4dd683bfd3b434c000292

from typing import List


def to_digits(number: int) -> List[int]:
    assert number > 0, "Negative numbers are not supported"
    return [int(digit) for digit in str(number)]


def is_digit_followed_by_zeros(number: int) -> bool:
    return set(to_digits(number)[1:]) == {0}


def is_palindrom(number: int) -> bool:
    return to_digits(number) == to_digits(number)[::-1]


def are_digits_sequential(number: int) -> bool:
    return str(number) in '9876543210' or str(number) in '1234567890'


def meets_criteria(number: int, awesome_phrases: List[int]):
    return number > 99 and (is_digit_followed_by_zeros(number) or number in awesome_phrases or is_palindrom(number)
                            or are_digits_sequential(number))


def is_interesting(number: int, awesome_phrases: List[int]) -> int:
    if meets_criteria(number, awesome_phrases):
        return 2
    if meets_criteria(number + 1, awesome_phrases) or meets_criteria(number + 2, awesome_phrases):
        return 1
    return 0
