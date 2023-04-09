#!/usr/bin/python3


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): The desired number of H characters in the file.

    Returns:
        int: The fewest number of operations needed to achieve 
	the desired number of H characters in the file,
             or 0 if it is impossible to achieve the desired number.
    """
    if n == 1:
        return 0

    num_chars = 1
    operations = 0

    while num_chars < n:
        if n % num_chars == 0:
            num_chars *= 2
            operations += 2
        else:
            num_chars += 1
            operations += 1

    if num_chars == n:
        return operations
    else:
        return 0
