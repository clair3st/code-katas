"""Solution for codewars katas."""


def find_uniq(arr):
    """Find unique string in a list of strings.

    https://www.codewars.com/kata/find-the-unique-string/train/python
    """
    from collections import Counter
    count = Counter(''.join(arr).lower())
    matching = [s for s in arr if min(count, key=count.get) in s.lower()]
    return matching[0]
