"""
@author: Saksham Goel
@description: Creating a neural network from scratch in python with no external libraries.
@version: 0.1
"""
# Imports
import matrix as mx

class NeuralNetwork(object):
    """
    The Simple Neural Network made by Saksham Goel
    """
    def __init__(self, weights: list[list[list[float]]], biases: list[list[float]], activation_type: str):
        self.weights = weights
        self.biases = biases
    
    def forward_pass(self, x):
        pass

    def backward_pass(self, x):
        pass


# File Loading/Saving Logic for the Neural Network Library
def load_neural_network(fileName: str):
    """
    :precondition: The .json must be formatted as
    :param fileName: The local file path to the model's structure (.json)
    :return: returns the loaded neural network
    """
    pass

def save_neural_network(fileName: str):
    pass


if __name__ == '__main__':
    # Mini tests
    print(transpose([[1, 2], [3, 4]]))