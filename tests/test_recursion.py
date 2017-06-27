"""Test recursive functions."""

import pytest


PARAMS = [
    (5, 15),
    (1, 1),
    (0, 0)
]

FIB_PARAMS = [
    (1, 1),
    (2, 1),
    (3, 2),
    (7, 13)
]


@pytest.mark.parametrize('n, result', PARAMS)
def test_sum_of_n(n, result):
    """Test factorial sumation."""
    from src.recursion_practise import sum_of_n
    assert sum_of_n(n) == result


@pytest.mark.parametrize('n, result', FIB_PARAMS)
def test_fib(n, result):
    """Test factorial sumation."""
    from src.recursion_practise import fibonacci
    assert fibonacci(n) == result
