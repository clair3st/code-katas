"""Module for sum pairs problem."""


def sum_pairs(ints, s):
    """Pair to sum up to s."""
    lookup = {}
    for n, i in enumerate(ints):
        lookup.setdefault(i, []).append(n)

    options = []

    for k in lookup:
        if s - k in lookup:
            if s - k == k and len(lookup[s - k]) < 2:
                continue
            if s - k == k and len(lookup[s - k]) >= 2:
                options.append(
                    [k,
                     s - k,
                     max(lookup[k])]
                )
                continue
            options.append(
                [k,
                 s - k,
                 max(min(lookup[k]), min(lookup[s - k]))]
            )
    print(options)

    if options:
        return sorted(min(options, key=lambda x: x[2])[:-1],
                      key=lookup.__getitem__)
    return None
