# Memoized Fibonacci
# https://www.codewars.com/kata/529adbf7533b761c560004e5

from functools import wraps


def cache(func):
    cache_dict = dict()

    @wraps(func)
    def func_wrapper(*args, **kwargs):
        n = args[0]
        if n not in cache_dict:
            cache_dict[n] = func(*args, **kwargs)
        return cache_dict[n]

    return func_wrapper


@cache
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
