"""Test array .diff."""

import pytest


LISTS = [
    [[1, 2], [1], [2]],
    [[1, 2, 2], [1], [2, 2]],
    [[1, 2, 2], [2], [1]],
    [[1, 2, 2], [], [1, 2, 2]],
    [[], [1, 2], []],
]


@pytest.mark.parametrize("n, x, result", LISTS)
def test_array_diff(n, x, result):
    """Test array diff for some value of n and x."""
    from src.array_diff import array_diff
    assert array_diff(n, x) == result
