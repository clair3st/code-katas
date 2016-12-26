"""Check if a string of parens is balanced, open or brokend."""

from stack import Stack


def proper_parens(str):
    """Return 0 if string of parens is balanced, 1 if open and -1 if broken."""
    stack = Stack()

    for i in str:

        if i is '(':
            stack.push(i)
            print('data', stack._container.head.data)
        elif i is ')':
            try:
                stack.pop()
            except IndexError:
                return -1

    if stack._container.head:
        return 1

    return 0
