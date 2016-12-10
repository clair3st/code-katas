"""Test power of two function for different values of n."""

import pytest


NUMS = [
    [0, [1]],
    [1, [1, 2]],
    [4, [1, 2, 4, 8, 16]]
]


@pytest.mark.parametrize("n, result", NUMS)
def test_powers_of_two(n, result):
    """Test powers of two for some value of n."""
    from powers_of_two import powers_of_two
    assert powers_of_two(n) == result
