# Reverse every other word in the string
# https://www.codewars.com/kata/reverse-every-other-word-in-the-string/


def reverse_alternate(string):
    words = string.split(" ")
    return " ".join([word[::-1] if words.index(word) % 2 != 0 else word for word in words])
