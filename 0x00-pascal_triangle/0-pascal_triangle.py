#!/usr/bin/env python3
"""
This module contains a function that generates Pascal's Triangle.

Pascal's Triangle is a triangular array of numbers where each
row is constructed by adding the two numbers above it to the left
and right. The outermost numbers of each row are always 1.
"""


def pascal_triangle(n):
    """
    Generate the first n rows of Pascal's Triangle.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing the first n rows of
        Pascal's Triangle. If n is less than or equal to 0,
        an empty list is returned.
    """
    if n <= 0:
        return []

    # Initialize the first row of the triangle
    triangle = [[1]]

    # Compute each row of the triangle
    for i in range(1, n):
        # Initialize a new row with
        # the first element set to 1
        row = [1]

        # Compute each element of the row
        # (except for the 1st & last elements)
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)

        # Set the last element of the row to 1
        # and append the row to the triangle
        row.append(1)
        triangle.append(row)

    return triangle
