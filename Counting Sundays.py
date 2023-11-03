def counting_sundays():
    date = [1, 1, 1901]
    months_with_30 = [4, 6, 9, 11]
    start = 365
    num_of_sundays = 0
    while date[2] < 2001:
        if start % 7 == 0:
            num_of_sundays += 1
            date[3]

