def find_outlier(integers):
    even_counter, odd_counter = 0, 0
    for number in integers:
        if number % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1

    if odd_counter > 1:
        for number in integers:
            if number % 2 == 0:
                return number
    else:
        for number in integers:
            if number % 2 == 1:
                return number
