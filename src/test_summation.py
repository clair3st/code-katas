"""Test summation function for values of n."""

import pytest


NUM = [
    [2, 3],
    [1, 1],
    [8, 36],
    [4, 10],
]


@pytest.mark.parametrize("n, result", NUM)
def test_summation(n, result):
    """Test summation returns expected sum."""
    from summation import summation
    assert summation(n) == result
