"""Test jenny's greeting function."""


import pytest

NAMES = [
    ["Johnny", "Hello, my love!"],
    ["James", "Hello, James!"],
]


@pytest.mark.parametrize("n, result", NAMES)
def test_greet(n, result):
    """Test jenny's greeting function."""
    from jenny_greet import greet
    assert greet(n) == result
