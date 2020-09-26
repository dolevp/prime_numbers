def two_or_odd_numbers_between(start, end):
    if start == 2:
        return [2, *range(3, end + 1, 2)]

    range_start = start + 1 if start % 2 == 0 else start
    return range(range_start, end + 1, 2)
