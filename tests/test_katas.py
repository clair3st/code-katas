"""Testing for completed katas."""

import pytest

PARAMS = [("LOL", 9),
          ("HOW R U", 13),
          ("WHERE DO U WANT 2 MEET L8R", 47),
          ("lol", 9),
          ("0", 2),
          ("ZER0", 11),
          ("1", 1),
          ("IS NE1 OUT THERE", 31),
          ("#", 1),
          ("#codewars #rocks", 36)]


PARAMS_SUM_PAIRS = [([1, 4, 8, 7, 3, 15], 8, [1, 7]),
                    ([1, -2, 3, 0, -6, 1], -6, [0, -6]),
                    ([20, -13, 40], -7, None),
                    ([1, 2, 3, 4, 1, 0], 2, [1, 1]),
                    ([10, 5, 2, 3, 7, 5], 10, [3, 7]),
                    ([4, -2, 3, 3, 4], 8, [4, 4]),
                    ([0, 2, 0], 0, [0, 0]),
                    ([5, 9, 13, -3], 10, [13, -3])
                    ]


PARAMS_UNIQ = [
    (['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a'], 'BbBb'),
    (['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba'], 'foo')
]

PARAMS_ALPHA = [
    ("The sunset sets at twelve o' clock.",
     "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"),
    (" ", "")
]


@pytest.mark.parametrize('s, result', PARAMS)
def test_phone_presses(s, result):
    """Test phone presses."""
    from src.phone_touch import presses_regex
    assert presses_regex(s) == result


@pytest.mark.parametrize('ints, s, result', PARAMS_SUM_PAIRS)
def test_sum_pairs(ints, s, result):
    """Test sum pairs."""
    from src.sum_pairs import sum_pairs
    assert sum_pairs(ints, s) == result


@pytest.mark.parametrize('lst, result', PARAMS_UNIQ)
def test_unique_string(lst, result):
    """Test unique string."""
    from src.kata import find_uniq
    assert find_uniq(lst) == result


@pytest.mark.parametrize('s, result', PARAMS_ALPHA)
def test_alphabet_position(s, result):
    """Test string alphabet position."""
    from src.kata import alphabet_position
    assert alphabet_position(s) == result
