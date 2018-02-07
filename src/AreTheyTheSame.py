def comp(array1, array2):
    if len(array1) == 0 or len(array2) == 0:
        return False
    else:
        array3 = [x**2 for x in array1]
        if sorted(array3) == sorted(array2) and len(array3) == len(array2):
            return True
        else:
            return False
