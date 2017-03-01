"""Stop trolls by removing all vowels of thier posts."""


def disemvowel(string):
    """Remove vowels of input string."""
    to_return = ''
    for char in string:
        if char not in 'aeiouAEIOU':
            to_return += char
    return to_return
