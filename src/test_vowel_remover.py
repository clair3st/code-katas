"""Test vowel remover function."""

import pytest


STRING = [
    ['hello', 'hll'],
    ['claire', 'clr'],
    ['borriquito como tu', 'brrqt cm t'],
    ['We are the Knights who say ni!', 'W r th Knghts wh sy n!'],
    ["It's just a flesh wound.", "It's jst  flsh wnd."]
]


@pytest.mark.parametrize("n, result", STRING)
def test_remove_vowels(n, result):
    """Test vowel remover correct items."""
    from vowel_remover import shortcut
    assert shortcut(n) == result
