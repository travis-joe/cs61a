def gcd(m, n):
    """Return the largest k that evenly divides both m and n.

    k, m, and n are all positive integers.

    >>> gcd(12, 8)
    4
    >>> gcd(16, 12)
    4
    >>> gcd(16, 8)
    8
    >>> gcd(2, 16)
    2
    >>> gcd(24, 42)
    6
    >>> gcd(5, 5)
    5
    """
    if n % m == 0:
        return m
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m - n, n)
