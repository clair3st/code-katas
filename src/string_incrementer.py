"""Increment number of string by one."""


def increment_string(strng):
    """String incrementer."""
    import re
    try:
        num = re.match('.*?([0-9]+)$', strng).group(1)
    except AttributeError:
        return strng + '1'
    s = strng.split(num)[0]
    new_num = str(int(num) + 1)
    if len(num) > len(new_num):
        z = len(num) - len(new_num)
        new_num = z * '0' + new_num
    return s + new_num
