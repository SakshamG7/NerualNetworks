"""
@author: Saksham Goel
@description: Creating a neural network from scratch in python with no external libraries.
@version: 0.1
"""
# Imports
import matrix as mx
from math_at_home import *
import json # Remove later and make your own parser.


class NeuralNetwork(object):
    """
    The Simple Neural Network made by Saksham Goel
    """
    def __init__(self, input_size: int = None, output_size: int = None, weights: list[list[list[float]]] = None, biases: list[list[float]] = None, activation_type: str = None):
        """
        Initializes the feed forward neural network.
        :param input_size: The number of inputs the model has.
        :param output_size: The number of outputs the model has.
        :param weights: The weights of the network.
        :param biases: The biases of the network.
        :param activation_type: The activation type of the neural network, e.g. sigmoid, ReLU, etc.
        """
        # Loads a very basic model if anything is missing
        if None in (input_size, output_size, weights, biases, activation_type):
            self.input_size: int = 1
            self.output_size: int = 1
            self.weights: list[list[list[float]]] = [[[1.0]]]
            self.biases: list[list[float]] = [[1.0]]
            self.activation_type: str = "sigmoid"
        else:
            self.input_size: int = input_size
            self.output_size: int = output_size
            self.weights: list[list[list[float]]] = weights
            self.biases: list[list[float]] = biases
            self.activation_type: str = activation_type

    def forward_pass(self, x):
        pass

    def backward_pass(self, x):
        pass


# File Loading/Saving Logic for the Neural Network Library
def load_neural_network(fileName: str) -> NeuralNetwork:
    """
    Loads the Neural Network file an d
    :file_conditions: The .json must be formatted as:
    {"version": 1, "input_size": int, "output_size": int, "weights": list[list[list[float]]], "biases": list[list[float]], "activation_type": str}
    :param fileName: The local file path to the model's structure (.json)
    :return: returns the loaded neural network
    """
    with open(fileName, "r") as f:
        # Yea, maybe later
        # for line in f:
            # dict(zip(*iter(line.split(':'))))
        data = json.loads(f.read())

    pass
    return NeuralNetwork()

def save_neural_network(fileName: str):
    pass


if __name__ == '__main__':
    # Mini tests
    print(mx.transpose([[1, 2], [3, 4]]))