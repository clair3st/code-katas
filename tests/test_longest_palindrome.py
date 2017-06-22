"""Test longest palindrome."""

import pytest


STRING = [
    ("a", 1),
    ("aa", 2),
    ("baa", 2),
    ("aab", 2),
    ("abcdefghba", 1),
    ("baablkj12345432133d", 9),
]


@pytest.mark.parametrize("n, result", STRING)
def test_longest_palidrome(n, result):
    """Test longest palindrome is found."""
    from src.longest_palindrome import longest_palindrome
    assert longest_palindrome(n) == result
