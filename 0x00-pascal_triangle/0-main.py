#!/usr/bin/env python3
"""
This module contains a function that prints Pascal's Triangle.

Pascal's Triangle is a triangular array of numbers where each
row is constructed by adding the two numbers above it to the left
and right. The outermost numbers of each row are always 1.
"""

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle


def print_triangle(triangle):
    """
    Print the triangle.

    Args:
        triangle (list): A list of lists representing
        the rows of Pascal's Triangle.

    Returns:
        None
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
