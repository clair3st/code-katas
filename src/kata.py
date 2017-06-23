"""Solution for codewars katas."""


def find_uniq(arr):
    """Find unique string in a list of strings.

    https://www.codewars.com/kata/find-the-unique-string/train/python
    """
    from collections import Counter
    count = Counter(''.join(arr).lower())
    matching = [s for s in arr if min(count, key=count.get) in s.lower()]
    return matching[0]


def alphabet_position(text):
    """Given text return string of position in alphabet.

    https://www.codewars.com/kata/replace-with-alphabet-position/python
    """
    return " ".join([str(ord(i) - 96) for i in text.lower()
                     if ord(i) > 96 and ord(i) < 123])
