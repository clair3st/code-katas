"""Function to remove vowel from input string."""


def shortcut(s):
    """Remove vowel from input string."""
    vowels = 'aeiou'
    new = ''
    for char in s:
        if char not in vowels:
            new += char
    return new
