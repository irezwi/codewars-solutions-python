def score(dice):
    triplets_points = [1000, 200, 300, 400, 500, 600]
    single_points = [100, 0, 0, 0, 50, 0]
    score = 0

    for number in range(1, 7):
        if dice.count(number) >= 3:
            score += triplets_points[number - 1]
        score += single_points[number - 1] * (dice.count(number) % 3)
    return score
