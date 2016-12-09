"""Function to return a reverse list of a integer."""


def digitize(n):
    """Return the reverse list of an integer."""
    a = [int(i) for i in str(n)]
    return a[::-1]
