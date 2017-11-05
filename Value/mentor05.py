def num_digits(n):
    """Takes in an positive integer and returns the number of
    digits.
    >>> num_digits(0)
    1
    >>> num_digits(1)
    1
    >>> num_digits(7)
    1
    >>> num_digits(1093)
    4
    """
    if n < 10:
        return 1
    else:
        return 1 + num_digits(n // 10)


def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    right_digit = n % 10
    rest = n // 10
    if rest == 0:
        return True
    elif right_digit > rest % 10:
        return False
    else:
        return is_sorted(rest)


def mario_number(level):
    """
    Return the number of ways that mario can traverse the
    level where mario can either hop by one digit or two
    digits each turn a level is defined as being an integer
    where a 1 is something mario can step on and 0 is
    something mario cannot step on.
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """
    if level == 1:
        return 1
    elif level % 10 == 0:
        return 0
    else:
        return mario_number(level // 10) + mario_number((level // 10) // 10)


def make_change(n):
    """Write a function, make_change that takes in an
    integer amount, n, and returns the minimum number
    of coins we can use to make change for that n,
    using 1-cent, 3-cent, and 4-cent coins.
    Look at the doctests for more examples.
    >>> make_change(5)
    2
    >>> make_change(6) # tricky! Not 4 + 1 + 1 but 3 + 3
    2
    """
    if n < 1:
        return 0
    elif n < 3:
        return 1 + make_change(n - 1)
    elif n < 4:
        use_1 = 1 + make_change(n - 1)
        use_3 = 1 + make_change(n - 3)
        return min(use_1, use_3)
    else:
        use_1 = 1 + make_change(n - 1)
        use_3 = 1 + make_change(n - 3)
        use_4 = 1 + make_change(n - 4)
        return min(use_1, use_3, use_4)
