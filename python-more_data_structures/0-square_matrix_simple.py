#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        square_row = [x ** 2 for x in row]
        new_matrix.append(square_row)
    return (new_matrix)
