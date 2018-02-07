def persistence(n):
    counter = 0
    while n > 9:
        n = multiply_digits(n)
        counter += 1
    return counter


def multiply_digits(n):
    result = 1
    for i in range(len(str(n))):
        result *= n % 10
        n = int(n / 10)
    return result
