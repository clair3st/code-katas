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


@pytest.mark.parametrize('s, result', PARAMS)
def test_phone_presses(s, result):
    """Test phone presses."""
    from phone_touch import presses_regex
    assert presses_regex(s) == result
