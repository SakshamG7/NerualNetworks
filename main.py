"""
@author: Saksham Goel
@description: Creating a neural network from scratch in python with no external libraries.
"""
from PIL.Image import radial_gradient


def load_neural_network(fileName: str):
    pass

def save_neural_network(fileName: str):
    pass

def transpose(x: list[list[float]]) -> list[list[float]]:
    # swaps rows and columns
    z: list[list[float]] = []
    for col in range(len(x[0])):
        z.append([])
        for row in range(len(x)):
            z[col].append(x[row][col])
    return z

def matrix_add(x: list[list[float]], y: list[list[float]]) -> list[list[float]]:
    if not (len(x) == len(y) and len(x[0]) == len(y[0])) or len(x) == 0 or len(y) == 0:
        return [[-1]]
    z: list[list[float]] = []
    for i in range(len(x)):
        z.append([])
        for j in range(len(x[0])):
            z[i].append(x[i][j] + y[i][j])
    return z


def matrix_mult(x, y) -> list:
    pass

class NeuralNetwork(object):
    def __init__(self, weights, biases):
        self.weights = weights
        self.biases = biases
    
    def forward_pass(self, x):
        pass

    def backward_pass(self, x):
        pass

if __name__ == '__main__':
    # Mini tests
    print(transpose([[1, 2]]))