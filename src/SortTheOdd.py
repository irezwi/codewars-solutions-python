# Sort the odd
# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d


def sort_array(source_array):
    odds_positions = []
    odds = []
    for index, number in enumerate(source_array):
        if number % 2 == 1:
            odds_positions.append(index)
            odds.append(number)
    odds = sorted(odds)
    for i in range(len(odds)):
        source_array[odds_positions[i]] = odds[i]
    return source_array
