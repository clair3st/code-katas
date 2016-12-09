"""Function to sum all numbers from 0 to n."""


def summation(num):
    """Return sum of 0 to num."""
    x = [i for i in range(num + 1)]
    return sum(x)
