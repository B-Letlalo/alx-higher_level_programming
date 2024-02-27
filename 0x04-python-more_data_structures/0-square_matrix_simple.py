#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    row = len(matrix)
    # Assuming all rows have the same length
    col = len(matrix[0])
    # Creating new matrix:
    new_matrix = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            new_matrix[i][j] = matrix[i][j]**2

    return(new_matrix)
