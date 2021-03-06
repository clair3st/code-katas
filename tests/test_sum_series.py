"""Test sum series function for different values of n."""

import pytest

NUMS = [
    [1, '1.00'],
    [2, '1.25'],
    [3, '1.39'],
    [5, '1.57'],
    [0, '0.00']
]


@pytest.mark.parametrize("n, result", NUMS)
def test_sum_series(n, result):
    """Test the addition of harmonic series."""
    from src.sum_series import sum_series
    assert sum_series(n) == result
