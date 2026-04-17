#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """returns the pascal triangle"""
    triangle = []
    if n < 0:
        return []
    for x in range(n):
        triangle.append([1])
        for y in range(0, x):
            if y == x - 1:
                triangle[x].append(1)
            else:
                triangle[x].append(triangle[x - 1][y] + triangle[x - 1][y + 1])
    return triangle
