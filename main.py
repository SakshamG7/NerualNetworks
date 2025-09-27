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
    def __init__(self, input_size: int = None, output_size: int = None, weights: list[list[list[float]]] = None, biases: list[list[float]] = None, activation_type: str = None) -> None:
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

    def forward_pass(self, x: list[float]) -> list[float]:
        """
        Generates a softmax output based on the input "x"
        :param x: Inputs
        :return: Returns the outputs of the model
        """
        pass

    def backward_pass(self, x: list[float], y: list[float]) -> None:
        """
        Performs a backward pass on the neural network to minimize loss and accelerate learning.
        :param x: Inputs
        :param y: expected outputs
        :return: Does not return anything.
        """
        pass
    
    def get_dict_structure(self) -> dict:
        """
        Get the structure of the Neural Network as a dictionary.
        :return: Returns the Model's Structure as a dictionary.
        """
        structure = {
            "version": 1,
            "input_size": self.input_size,
            "output_size": self.output_size,
            "weights": self.weights,
            "biases": self.biases,
            "activation_type": self.activation_type
        }
        return structure

    def __repr__(self) -> str:
        return str(self.get_dict_structure())


# File Loading/Saving Logic for the Neural Network Library
def load_neural_network(fileName: str) -> NeuralNetwork:
    """
    Loads the Neural Network file from fileName.
    :precondition: The .json must be formatted as:
    {
        "version": 1, "input_size": int,
        "output_size": int,
        "weights": list[list[list[float]]],
        "biases": list[list[float]],
        "activation_type": str
    }
    :param fileName: The local file path to the model's structure (.json)
    :return: Returns the loaded neural network
    """
    with open(fileName, "r") as f:
        # Yea, maybe later
        # for line in f:
            # dict(zip(*iter(line.split(':'))))
        data = json.loads(f.read())
    return NeuralNetwork(data["input_size"], data["output_size"], data["weights"], data["biases"], data["activation_type"])


def save_neural_network(fileName: str, model: NeuralNetwork) -> None:
    """
    Saves the Neural Network "model" to json file.
    :param fileName: The local file path to the model's structure (.json)
    :param model: The model to be saved.
    :return: This function does not return anything.
    """
    with open(fileName, "w") as f:
        json.dump(model.get_dict_structure(), f)


if __name__ == '__main__':
    # Mini tests
    print(mx.transpose([[1, 2], [3, 4]]))
