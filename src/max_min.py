"""Function to return max and min in a list."""


def min_cw(l):
    """Return min value of a list."""
    a = sorted(l)
    return a[0]


def max_cw(l):
    """Return max value of a list."""
    a = sorted(l)
    return a[-1]
