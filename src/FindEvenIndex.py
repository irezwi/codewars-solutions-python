# Equal Sides Of An Array
# https://www.codewars.com/kata/5679aa472b8f57fb8c000047


def find_even_index(arr):
    right = 0
    left = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            right += arr[j]
        for k in range(0, i - 1 + 1):
            left += arr[k]
        if right == left:
            print(i)
            return i
        right = 0
        left = 0
    return -1
