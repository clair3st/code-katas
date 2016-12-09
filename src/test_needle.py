"""Test find_needle function."""

import pytest

NAMES = [
    [['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'], "5"],
    [[1, 'stuff', 'needle'], '2']
]


@pytest.mark.parametrize("n, result", NAMES)
def test_greet(n, result):
    """Test jenny's greeting function."""
    from needle import find_needle
    assert find_needle(n)[-1] == result
