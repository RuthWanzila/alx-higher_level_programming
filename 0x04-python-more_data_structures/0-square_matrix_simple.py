#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        squared_row = map(lambda num: num**2, row)
        result_matrix.append(list(squared_row))
    return result_matrix
