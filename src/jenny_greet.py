"""Debug Jenny's greeting function."""


def greet(name):
    """Greet message, formatted differently for johnny."""
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
