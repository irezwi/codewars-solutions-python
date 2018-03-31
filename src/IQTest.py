# IQTest
# https://www.codewars.com/kata/552c028c030765286c00007d


def iq_test(numbers):
    odd, even = 0, 0  # Counters of even and odd numbers
    numbers = list(numbers.split(" "))  # Returns list of numbers represented by strings
    for number in numbers:
        if int(number) % 2 == 0:
            even += 1
        else:
            odd += 1
        # If one of counters is bigger or equal 2 we don't have to search anymore
        if even >= 2:
            return numbers.index([x for x in numbers if int(x) % 2 == 1][0]) + 1
        elif odd >= 2:
            return numbers.index([x for x in numbers if int(x) % 2 == 0][0]) + 1
