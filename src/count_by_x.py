"""Return list of values that are multiplies of x."""


def count_by(x, n):
    """Return a sequence of numbers counting by `x` `n` times."""
    return [i * x for i in range(1, n + 1)]
