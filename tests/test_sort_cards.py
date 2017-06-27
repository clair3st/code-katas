"""Test sort cards functions."""

import pytest


CARDS = [
    [['A'], ['A']],
    [['3'], ['3']],
    [['T'], ['T']],
    [['T', '8', '2', '4', 'Q'], ['2', '4', '8', 'T', 'Q']],
    [['Q', 'K', 'J', '6', '9', '3', '2'], ['2', '3', '6', '9', 'J', 'Q', 'K']],
    [['J', '6', '9', '3', '2', '7', 'A', '8'], ['A', '2', '3', '6', '7', '8', '9', 'J']],
    [['J', '6', '7', '9', 'J', '7', '3', '2', '7', 'A', '8'], ['A', '2', '3', '6', '7', '7', '7', '8', '9', 'J', 'J']],
    [['T', 'A', '8', 'A', 'A', 'A', '2', '4', 'A', 'Q', 'A'], ['A', 'A', 'A', 'A', 'A', 'A', '2', '4', '8', 'T', 'Q']],
]


def test_sort_cards_returns_same_length():
    """Test sort cards doesn't change the length of input list."""
    from src.sort_cards import sort_cards
    cards = ['Q', 'K', 'J', '6', '9', '3', '2']
    assert len(sort_cards(cards)) == len(cards)


@pytest.mark.parametrize("cards, result", CARDS)
def test_sort_cards(cards, result):
    """Test sort card method on differect card inputs."""
    from src.sort_cards import sort_cards
    assert sort_cards(cards) == result
