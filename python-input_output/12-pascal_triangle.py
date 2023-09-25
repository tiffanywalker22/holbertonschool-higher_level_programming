#!/usr/bin/python3
# 12-pascal_triangle.py
# Tiffany Walker
""" function returns a list of lists of ints """


def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for x in range(1, i):
            new_row.append(prev_row[x - 1])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
