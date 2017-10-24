def has_sum(total, n, m):
    """
    >>> has_sum(1, 3, 5) False

    >>> has_sum(5, 3, 5) # 0 * 3 + 1 * 5 = 5 True

    >>> has_sum(11, 3, 5) # 2 * 3 + 1 * 5 = 11 True

    """
    if total == 0 or total == m or total == n:
        return True
    elif total < min(m, n):
        return False
    return has_sum(total - n, n, m) or has_sum(total - m, n, m)


def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer 1 prints within this range True

    >>> sum_range(40, 55) # Printer 1 can print a number 56-60 False

    >>> sum_range(170, 201) # Printer 1 + 2 will print between 180 and 200
        copies total True
    """

    def copies(pmin, pmax):
        if lower <= pmin and pmax <= upper:

            return
        elif:

            return
        return

        return copies(0, 0)
