"""Test disemvowel function for different values of n."""

import pytest


STRINGS = [
    ["This website is for losers LOL!", "Ths wbst s fr lsrs LL!"],
    ["No offense but,\nYour writing is among the worst I've ever read",
     "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"],
]


@pytest.mark.parametrize("string, result", STRINGS)
def test_disemvowel(string, result):
    """Test disemvowel for some string."""
    from src.disemvowel import disemvowel
    assert disemvowel(string) == result
