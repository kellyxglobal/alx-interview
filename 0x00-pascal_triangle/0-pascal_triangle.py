#!/usr/bin/python3
"""
0-main
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the first row of the triangle
    triangle = [[1]]

    # Compute each row of the triangle
    for i in range(1, n):
        # Initialize a new row with the first element set to 1
        row = [1]

        # Compute each element of the row (except for the first and last elements)
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)

        # Set the last element of the row to 1 and append the row to the triangle
        row.append(1)
        triangle.append(row)

    return triangle

