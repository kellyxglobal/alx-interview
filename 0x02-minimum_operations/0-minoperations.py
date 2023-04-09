#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
    n (int): The number of H characters needed.

    Returns:
    int: The fewest number of operations needed to obtain n H characters. Returns 0 if n is impossible to achieve.
    """

    if n < 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1

    return operations
