"""Test change calculator."""


def test_change_calculator():
    """Test change calculator."""
    from change import change
    assert change(11) is 3
