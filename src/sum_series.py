"""Sum of the first nth value of a series."""


def sum_series(n):
    """Sum of the first nth value of a series."""
    a = sum([1.0 / (3 * i + 1) for i in range(n)])
    return '{number:.{digits}f}'.format(number=a, digits=2)


# source sum of harmonic progression
# (https://en.wikipedia.org/wiki/Harmonic_progression_(mathematics))
