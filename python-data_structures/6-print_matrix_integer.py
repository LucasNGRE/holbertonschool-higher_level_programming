#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:  # Check if the row is not empty
            print(" ".join("{:d}".format(num) for num in row))
