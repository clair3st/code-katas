"""Test double char function."""

import pytest


S = [
    ["String", "SSttrriinngg"],
    ["Hello World", "HHeelllloo  WWoorrlldd"],
    ["1234!_ ", "11223344!!__  "]
]


@pytest.mark.parametrize("s, result", S)
def test_double_char(s, result):
    """Test double char for some value of s."""
    from src.double_char import double_char
    assert double_char(s) == result
