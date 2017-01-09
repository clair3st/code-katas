"""Sort a deck of cards using a python algorithm."""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    reference:
    http://pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/

    """
    card_order = {'A': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    return sorted(cards, key=card_order.__getitem__)
