# Exes and Ohs
# https://www.codewars.com/kata/55908aad6620c066bc00002a


def xo(s):
    s = s.lower()
    x = 0
    o = 0

    for letter in s:
        if letter == 'x':
            x += 1
        elif letter == 'o':
            o += 1
    if x == o:
        return True
    else:
        return False
