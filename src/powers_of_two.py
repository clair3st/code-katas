"""Function to return list of powers of 2 for n."""


def powers_of_two(n):
    """Return power of 2 of length n."""
    return [2**i for i in range(n + 1)]
