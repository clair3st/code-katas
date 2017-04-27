"""Test string incrementer."""

import pytest

STRINGS = [
    ["foo", "foo1"],
    ["foobar001", "foobar002"],
    ["foobar1", "foobar2"],
    ["foobar00", "foobar01"],
    ["foobar99", "foobar100"],
    ["foobar099", "foobar100"],
    ["", "1"]
]


@pytest.mark.parametrize("n, result", STRINGS)
def test_sum_square(n, result):
    """Test the string incrementer."""
    from string_incrementer import increment_string
    assert increment_string(n) == result
