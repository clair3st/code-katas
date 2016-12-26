"""Test proper parenthetics."""

import pytest


EXAMPLE_PARENS = [
    ['()()()', 0],
    ['(()', 1],
    ['(()))', -1],
    [')))(((', -1],
    ['(sdg)', 0],
    ['(hi', 1]
]


@pytest.mark.parametrize("parens, result", EXAMPLE_PARENS)
def test_proper_parens(parens, result):
    """Test proper parens returns correct result for given cases."""
    from proper_parenthetics import proper_parens
    assert proper_parens(parens) == result
