def find_outlier(integers):
    if len(integers) % 2 == 1 and sum(integers) % 2 == 0:
        for number in integers:
            if number % 2 == 0:
                return number
    else:
        for number in integers:
            if number % 2 == 1:
                return number
