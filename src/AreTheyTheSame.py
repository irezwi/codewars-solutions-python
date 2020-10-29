# Are they the "same"?
# https://www.codewars.com/kata/550498447451fbbd7600041c


def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    return sorted(list(map(lambda x: x ** 2, array1))) == sorted(array2)
