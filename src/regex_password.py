"""Regex password evaluator."""

import re


def regex_validator(password):
    """Test input strings for correct password arragement.

    Requires minimum 6 characters, 1 lower case, 1 upper and 1 number.
    """
    return bool(re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$",
                password))
