# Are they the "same"?
# https://www.codewars.com/kata/550498447451fbbd7600041c


import math


def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    else:
        for i in range(0, len(array2)):
            if math.sqrt(array2[i]) not in array1:
                return False
        return True
