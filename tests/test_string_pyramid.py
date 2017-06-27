"""Test the string pyramid method."""

import pytest

PYRAMID_SIDE = [
    [None, None],
    ['', ''],
    ['*#', ' # \n***'],
    ['abc', '  c  \n bbb \naaaaa'],
    ['aa', ' a \naaa'],
    ['321', '  1  \n 222 \n33333']
]

PYRAMID_TOP = [
    [None, None],
    ['', ''],
    ['*#', '***\n*#*\n***'],
    ['abc', 'aaaaa\nabbba\nabcba\nabbba\naaaaa'],
    ['aa', 'aaa\naaa\naaa'],
    ['321', '33333\n32223\n32123\n32223\n33333'],

]

OUTER_COUNT = [
    [None, -1],
    ['', -1],
    ['*#', 9],
    ['abc', 25],
    ['aa', 9],
    ['321', 25]
]

INNER_COUNT = [
    [None, -1],
    ['', -1],
    ['*#', 10],
    ['abc', 35],
    ['aa', 10],
    ['321', 35]
]


@pytest.mark.parametrize("n, result", PYRAMID_SIDE)
def test_side_view(n, result):
    """Test side view returns side view of a pyramid."""
    from src.string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side(n) == result


@pytest.mark.parametrize("n, result", PYRAMID_TOP)
def test_top_view(n, result):
    """Test side view returns side view of a pyramid."""
    from src.string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above(n) == result


@pytest.mark.parametrize("n, result", OUTER_COUNT)
def test_count_outside(n, result):
    """Test count outside of the pyramid."""
    from src.string_pyramid import count_visible_characterss_of_the_pyramid
    assert count_visible_characterss_of_the_pyramid(n) == result


@pytest.mark.parametrize("n, result", INNER_COUNT)
def test_count_all(n, result):
    """Test count all blocks in the pyramid."""
    from src.string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid(n) == result
