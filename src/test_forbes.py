"""Test for forbes oldest and youngest algorithm."""

import pytest

YOUNGEST = [
    ['name', 'Mark Zuckerberg'],
    ['age', 32],
    ['net_worth (USD)', 44600000000],
    ['source', 'Facebook'],
]


OLDEST = [
    ['name', 'Phil Knight'],
    ['age', 78],
    ['net_worth (USD)', 24400000000],
    ['source', 'Nike'],
]


@pytest.mark.parametrize("key, result", YOUNGEST)
def test_youngest_person(key, result):
    """Test that youngest with a valid age is MarK Zuckerberg."""
    from forbes import youngest_and_oldest_under_eighty
    youngest = youngest_and_oldest_under_eighty()[0]
    assert youngest[key] == result


@pytest.mark.parametrize("key, result", OLDEST)
def test_oldest_person(key, result):
    """Test that oldest with a valid age is MarK Zuckerberg."""
    from forbes import youngest_and_oldest_under_eighty
    oldest = youngest_and_oldest_under_eighty()[1]
    assert oldest[key] == result


def test_result_has_no_rank():
    """Test that the result has only required fields."""
    from forbes import youngest_and_oldest_under_eighty

    assert 'rank' not in youngest_and_oldest_under_eighty()[0]
    assert 'rank' not in youngest_and_oldest_under_eighty()[1]


def test_result_has_no_country():
    """Test that the result has only required fields."""
    from forbes import youngest_and_oldest_under_eighty

    assert 'country' not in youngest_and_oldest_under_eighty()[0]
    assert 'country' not in youngest_and_oldest_under_eighty()[1]
