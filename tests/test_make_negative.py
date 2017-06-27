"""Test make negative number function for values of n."""

import pytest


NUM = [
    [2, -2],
    [-1, -1],
    [-8, -8],
    [10, -10],
]


@pytest.mark.parametrize("n, result", NUM)
def test_make_negative(n, result):
    """Test make_negative returns expected value."""
    from src.make_negative import make_negative
    assert make_negative(n) == result
