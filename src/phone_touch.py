"""Module for many katas."""


def presses(phrase):  # pragma: no cover
    """Given an old phone, how many touches for a given phrase."""
    key_pad = {'1ADGJMPTW ': 1, 'BEHKNQUX0': 2, 'CFILORVY': 3,
               'SZ234568': 4, '79': 5}
    presses = 0
    for i in phrase.upper():
        for k, v in key_pad.items():
            if i in k:
                presses += v
    return presses


def presses_regex(phrase):
    """Given an old phone, how many touches for a given phrase."""
    import re
    key_pad = {'1ADGJMPTW': 1, 'BEHKNQUX0': 2, 'CFILORVY': 3,
               'SZ234568': 4, '79': 5, '?!\W': 1}
    presses = 0
    for k, v in key_pad.items():
        presses += v * len(''.join(
            re.findall('[{}]*'.format(k), phrase.upper())
        ))
    return presses
