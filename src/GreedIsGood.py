def score(dice):
    points = 0
    d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for number in dice:
        d[number] += 1
    if d[1] >= 3:
        points += 1000
        d[1] -= 3
    for number in range(2, 7):
        if d[number] >= 3:
            points += 100 * number
            d[number] -= 3
    if d[5] != 0:
        points += 50 * d[5]
    if d[1] != 0:
        points += 100 * d[1]
    return points
