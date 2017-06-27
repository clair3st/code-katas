"""Test regex password validator."""

import pytest


STRINGS = [
    ['fjd3IR9', True],
    ['ghdfj32', False],
    ['DSJKHD23', False],
    ['dsF43', False],
    ['4fdg5Fj3', True],
    ['DHSJdhjsU', False],
    ['fjd3IR9.;', False],
    ['fjd3  IR9', False],
    ['djI38D55', True],
    ['a2.d412', False],
    ['JHD5FJ53', False],
    ['!fdjn345', False],
    ['jfkdfj3j', False],
    ['123', False],
    ['abc', False],
    ['123abcABC', True],
    ['ABC123abc', True],
    ['Password123', True]
]


@pytest.mark.parametrize("n, result", STRINGS)
def test_regex(n, result):
    """Test the string incrementer."""
    from src.regex_password import regex_validator
    assert regex_validator(n) is result
