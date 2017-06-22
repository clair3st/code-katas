"""Test the square_sum function."""


import pytest

NUMS = [
    [[1, 2], 5],
    [[0, 3, 4, 5], 50],
]


@pytest.mark.parametrize("n, result", NUMS)
def test_sum_square(n, result):
    """Test the sum of squares of a list is returned."""
    from src.square_sum import square_sum
    assert square_sum(n) == result
