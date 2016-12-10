"""Test opposite number function for values of n."""

import pytest


NUM = [
    [2, -2],
    [1, -1],
    [8, -8],
    [10, -10],
]


@pytest.mark.parametrize("n, result", NUM)
def test_opposite(n, result):
    """Test opposite returns expected sum."""
    from opposite_number import opposite
    assert opposite(n) == result
