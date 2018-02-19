def backwards_prime(start, stop):
    result = []
    for i in range(start, stop + 1):
        if is_backwards_prime(i):
            result.append(i)
    return result


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def is_backwards_prime(n):
    return n >= 10 and is_prime(n) and is_prime(reverse(n)) and n != reverse(n)


def reverse(n):
    return int(str(n)[::-1])
