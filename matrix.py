"""
@author: Saksham Goel
@description: Matrix operations using lists. (we have numpy at home)
@version: 1.0
"""

def transpose(x: list[list[float]]) -> list[list[float]]:
    """
    Transposes the matrix (swaps rows and columns) of tensor "x"
    :param x: The tensor to be transposed.
    :return: Transposed tensor.
    """
    z: list[list[float]] = []
    for col in range(len(x[0])):
        z.append([])
        for row in range(len(x)):
            z[col].append(x[row][col])
    return z

def matrix_sum(x: list[list[float]], y: list[list[float]]) -> list[list[float]]:
    """
    Adds two matrices together.
    :param x: The first tensor.
    :param y: The second tensor to be added to the first.
    :return: Returns the sum of the two tensors.
    """
    if not (len(x) == len(y) and len(x[0]) == len(y[0])) or len(x) == 0 or len(y) == 0:
        return [[-1]]
    z: list[list[float]] = []
    for i in range(len(x)):
        z.append([])
        for j in range(len(x[0])):
            z[i].append(x[i][j] + y[i][j])
    return z


def matrix_mult(x: list[list[float]], y: list[list[float]]) -> list[list[float]]:
    """
    Gets the multiplication product of the two matrices.
    :param x: The first tensor.
    :param y: The second tensor to be multiplied to the first.
    :return: Returns the product of the two tensors.
    """
