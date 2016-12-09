"""Test string to list function."""

import pytest


LIST = [
    ['Hello Hello Again', ['Hello', 'Hello', 'Again']],
    ['Test', ['Test']],
    ['', ['']],
    ['1 2 3', ['1', '2', '3']],
]


@pytest.mark.parametrize("n, result", LIST)
def test_string_list(n, result):
    """Test string is converted to list."""
    from string_to_list import string_to_array
    assert string_to_array(n) == result
