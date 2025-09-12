#!/usr/bin/python3
"""
Module 2-matrix_divided
This module contains a function matrix_divided that divid all elements
of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix rounded to  2 decimal places

    Args:
        matrix is a list of integers or floats .
        div is a number 

    Returns:
        a new matrix
    Raises:
        TypeError: If there are not integers or floats
        or if the row are not the same size
        ZeroDivisionError: if div = 0
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len({len(row) for row in matrix}) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
