"""Function to return list from string."""


def string_to_array(string):
    """Return a list from input string."""
    if string == "":
        return [""]
    return string.split()
