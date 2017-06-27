"""Test digitize function for different values of n."""

import pytest


NUMS = [
    [1, 5, [1, 2, 3, 4, 5]],
    [2, 5, [2, 4, 6, 8, 10]],
    [100, 4, [100, 200, 300, 400]]
]


@pytest.mark.parametrize("n, x, result", NUMS)
def test_count_by_x(n, x, result):
    """Test count_by_x for some value of n."""
    from src.count_by_x import count_by
    assert count_by(n, x) == result
