"""Return a list removing elements specified in another."""


def array_diff(a, b):
    """Return a after removing elements from b."""
    return [i for i in a if i not in b]
