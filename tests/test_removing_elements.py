"""Test remove every other element function."""

import pytest


LIST = [
    [['Hello', 'Goodbye', 'Hello Again'], ['Hello', 'Hello Again']],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]],
    [[[1, 2]], [[1, 2]]],
    [[['Goodbye'], {'Great': 'Job'}], [['Goodbye']]],
]


@pytest.mark.parametrize("n, result", LIST)
def test_remove_everey_other(n, result):
    """Test remove every other removes correct items."""
    from src.removing_elements import remove_every_other
    assert remove_every_other(n) == result
