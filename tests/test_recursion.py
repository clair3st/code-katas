"""Test recursive functions."""

import pytest


PARAMS = [
    (5, 15),
    (1, 1),
    (0, 0)
]


@pytest.mark.parametrize('n, result', PARAMS)
def test_sum_of_n(n, result):
    """Test factorial sumation."""
    from src.recursion_practise import sum_of_n
    assert sum_of_n(n) == result
