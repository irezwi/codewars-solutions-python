# Moving Zeros To The End
# https://www.codewars.com/kata/52597aa56021e91c93000cb0


def move_zeros(array):
    zeros, arr = [], []
    for number in array:
        if not isinstance(number, bool) and number == 0:
            zeros.append(0)
        else:
            arr.append(number)
    return arr + zeros


a = ["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]
print(move_zeros(a))
