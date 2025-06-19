#!/usr/bin/python3
"""Module for generating Pascal's triangle of size n."""

def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n rows."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(1, len(prev)):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)
    return triangle
