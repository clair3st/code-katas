"""Test even or odd function."""

import pytest

NUMBERS = [
    [2, 'Even'],
    [0, 'Even'],
    [7, 'Odd'],
    [1, 'Odd'],
]


@pytest.mark.parametrize("n, result", NUMBERS)
def test_even_or_odd(n, result):
    """Test even or odd for some value of n."""
    from evenorodd import even_or_odd
    assert even_or_odd(n) == result
