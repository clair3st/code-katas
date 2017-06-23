"""Practise recursion thanks to Nick."""

# 1. Write a function that takes a number N and adds up all the numbers
# from 0 to N using recursion

# 2. Write a function that generates the Nth number of the Fibonacci sequence
# using recursion

# 3. Write a function that walks through a singly-linked list and returns
# the value at the tail of the list using recursion

# 4. Write a function that returns every even number in a linked list of
# only numerical values using recursion

# 5. A factorial is defined as the product of every number from 1 up to N,
# so 5 factorial (aka 5!) is 5 * 4 * 3 * 2 * 1. Write a function that takes
# a single integer N and returns the sum of every factorial up to and
# including N.
# So if N = 5 it'd return 5! + 4! + 3! + 2! + 1!. Try and see how high you
# can get N before you reach the maximum recursion depth.


def sum_of_n(n):
    """Sum all numbers from 0 to N, recursively."""
    if n == 0:
        return 0
    return n + sum_of_n(n - 1)


def fibonacci(n):
    """Return the nth number of the fibonacci series."""
    if n is 1 or n is 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
