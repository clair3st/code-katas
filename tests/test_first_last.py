"""Tests for the first and last function."""


import pytest


STRING = [
    ['hello', 'ell'],
    ['claire', 'lair'],
    ['borriquito como tu', 'orriquito como t'],
    ['We are the Knights who say ni!', 'e are the Knights who say ni'],
    ["It's just a flesh wound.", "t's just a flesh wound"]
]


@pytest.mark.parametrize("n, result", STRING)
def test_first_last(n, result):
    """Test first and last character is removed."""
    from src.first_last import remove_char
    assert remove_char(n) == result
