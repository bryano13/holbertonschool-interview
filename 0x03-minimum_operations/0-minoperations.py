#!/usr/bin/python3
"""
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns an integer. If n is impossible to achieve, return 0.
    """

    current = 1
    numberOperations = 0
    buffer = 0

    if n < 2:
        return 0

    while current < n:
        rest = n - current

        if rest % current == 0:
            buffer = current
            current += buffer
            numberOperations += 2

        else:
            current += buffer
            numberOperations += 1

    return numberOperations
