"""Tests max and min functions."""


import pytest

MIN_NUMBERS = [
    [[-52, 56, 30, 29, -54, 0, -110], -110],
    [[4, 6, 2, 1, 9, 63, -134, 566], -134],
    [[1, 2, 3, 4, 5, 10], 1],
    [[-1, -2, -3, -4, -5, -10], -10],
    [[9], 9]
]

MAX_NUMBERS = [
    [[-52, 56, 30, 29, -54, 0, -110], 56],
    [[42, 54, 65, 87, 0], 87],
    [[5], 5],
    [[534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555], 555],
    [[9], 9]
]


@pytest.mark.parametrize("n, result", MIN_NUMBERS)
def test_min(n, result):
    """Test min for some value of n."""
    from src.max_min import min_cw
    assert min_cw(n) == result


@pytest.mark.parametrize("n, result", MAX_NUMBERS)
def test_max(n, result):
    """Test max for some value of n."""
    from src.max_min import max_cw
    assert max_cw(n) == result
