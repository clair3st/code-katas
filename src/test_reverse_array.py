"""Test digitize function for different values of n."""

import pytest


NUMS = [
    [35231, [1, 3, 2, 5, 3]],
    [176, [6, 7, 1]],
    [4, [4]]
]


@pytest.mark.parametrize("n, result", NUMS)
def test_digitize(n, result):
    """Test digitize for some value of n."""
    from reverse_array import digitize
    assert digitize(n) == result
