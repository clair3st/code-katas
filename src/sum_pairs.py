"""Module for sum pairs problem."""


def sum_pairs(ints, s):
    """Pair to sum up to s."""
    lookup = {}
    for n, i in enumerate(ints):
        lookup.setdefault(i, n)
    options = [[k, (s - k)] for k in lookup if (s - k) in lookup]
    if options:
        return min(options, key=lambda x: lookup[x[0]])
    return None
