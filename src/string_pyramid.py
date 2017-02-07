"""Build a pyramid out of a string."""


def watch_pyramid_from_the_side(chars):
    """View the pyramid from the side."""
    if chars:
        result = []
        odd = [x * 2 + 1 for x in range(len(chars))]
        for i, x in enumerate(chars[::-1]):
            layer = x * odd[i]
            space = (odd[-1] - len(layer)) // 2 * ' '
            result.append(space + layer + space)
        return '\n'.join(result)
    return chars


def watch_pyramid_from_above(chars):
    """View the pyramid from above."""
    if chars:
        result = []
        odd = [x * 2 + 1 for x in reversed(range(len(chars)))]
        odd.extend(odd[:-1][::-1])
        chars += chars[:-1][::-1]
        for i, x in enumerate(chars):
            layer = x * odd[i]
            space = (odd[0] - len(layer)) // 2
            result.append(chars[:space] + layer + chars[:space][::-1])
        return '\n'.join(result)
    return chars


def count_visible_characterss_of_the_pyramid(chars):
    """Count block of the pyramid visible from the outside."""
    if chars:
        return ((len(chars) - 1) * 2 + 1) ** 2
    else:
        return -1


def count_all_characters_of_the_pyramid(chars):
    """Count all block in the pyramid."""
    if chars:
        return sum([(x * 2 + 1) ** 2 for x in range(len(chars))])
    else:
        return -1
