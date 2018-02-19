# Friend or Foe?
# https://www.codewars.com/kata/55b42574ff091733d900002f


def friend(x):
    result = []
    for item in x:
        if len(item) == 4:
            result.append(item)
    return result
