"""Forbes 40 billionaires list."""

from src.flight_path import get_data_from_json_file


def youngest_and_oldest_under_eighty():
    """Using forbes data return the youngest and oldest under 80.

    Challenge, not using sort function.
    """
    data = get_data_from_json_file('src/rich-ppl.json')

    min_age = {'age': 100}
    max_age = {'age': 20}

    for idx in data:
        if 0 < idx['age'] < min_age['age']:
            min_age = idx
        if max_age['age'] < idx['age'] < 80:
            max_age = idx

    min_age.pop('country', None)
    max_age.pop('country', None)
    min_age.pop('rank', None)
    max_age.pop('rank', None)

    return min_age, max_age


def display_result(ages):  # pragma: no cover
    """Display oldes and youngest."""
    print("""Youngest Billionare:
    {name}, {age} years old, with net worth of ${net_worth (USD)} from {source}""".format(**ages[0]))
    print("""Oldest Billionare (under 80):
    {name}, {age} years old, with net worth of ${net_worth (USD)} from {source}""".format(**ages[1]))


if __name__ == '__main__':   # pragma: no cover
    display_result(youngest_and_oldest_under_eighty())
