"""
@author: Saksham Goel
@description: Matrix operations using lists. (we have numpy at home)
@version: 2.0
"""

def transpose(x: list[list[float]]) -> list[list[float]]:
    """
    Transposes the matrix 90 degrees anti-clockwise (swaps rows and columns) of tensor "x"
    :param x: The tensor to be transposed.
    :return: Transposed tensor.
    """
    z: list[list[float]] = []
    for col in range(len(x[0]), 0, -1):
        z.append([])
        for row in range(len(x)):
            z[-1].append(x[row][col-1])
    return z

def matrix_sum(x: list[list[float]], y: list[list[float]]) -> list[list[float]]:
    """
    Adds two matrices together.
    :param x: The first tensor.
    :param y: The second tensor to be added to the first.
    :return: Returns the sum of the two tensors.
    """
    if not (len(x) == len(y) and len(x[0]) == len(y[0])) or len(x) == 0 or len(y) == 0:
        return [[-1.0]]
    z: list[list[float]] = []
    for i in range(len(x)):
        z.append([])
        for j in range(len(x[0])):
            z[i].append(x[i][j] + y[i][j])
    return z


def simple_vector_dot_product(x: list[float], y: list[float]) -> float:
    """
    Gets the multiplication product of the two simple vectors.
    :param x: The first tensor.
    :param y: The second tensor to be multiplied to the first.
    :return: Returns the dot product of the two tensors.
    """
    if len(y) != len(x):
        return -1.0
    z: float = 0.0
    for i in range(len(x)):
        z += x[i] * y[i]
    return z

def matrix_mult(x: list[list[float]], y: list[list[float]]) -> list[list[float]]:
    """
    Gets the multiplication product of the two matrices.
    :param x: The first tensor.
    :param y: The second tensor to be multiplied to the first.
    :return: Returns the product of the two tensors.
    """
    # Number of rows in "y" must match the number of columns in "x"
    if len(y) != len(x[0]):
        return [[-1.0]]

    y_t: list[list[float]] = transpose(y)
    z: list[list[float]] = [[] for _ in x]

    for i in range(len(y_t)):
        for j in range(len(x)):
            dot_prod = simple_vector_dot_product(x[j], y_t[-1 - i])
            z[j].append(dot_prod)

    return z

if __name__ == '__main__':
    # mini tests
    # y_t_ = transpose([[2, 5],[6, 7],[1, 8]])
    # y_t_ = [[2, 5],[6, 7],[1, 8]]
    # print(y_t_)
    # print([[0.0] * len(y_t_[0])] * len(y_t_))
    # a1 = [1, 2, 3]
    # a2 = [2, 3, 6]
    # o = simple_vector_dot_product(a1, a2) # should be 26
    # print(o) # 26.0
    # print(matrix_mult([[1,2,1],[0,1,0],[2,3,4]], [[2, 5],[6, 7],[1, 8]]))
    pass
