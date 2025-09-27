"""
@author: Saksham Goel
@description: We have math at home
@version: 1.0
"""
# Constants
EUCLIDS_NUMBER: float = 2.718281828459045
PI: float = 3.141592653589793

def exp(x: float) -> float:
    """
    Computes and approximation of e**x.
    :param x: The exponent.
    :return: returns e to the power of x.
    """
    return EUCLIDS_NUMBER ** x

def log(x: float, base: float) -> float:
    """
    Computes and approximation of log based "base: of x.
    :param x: The input of the log function.
    :param base: The base of the log (e.g. 2, 10, e, etc.).
    :return: returns log_base(x), log base "base" of x.
    """
    return ln(x) / ln(base)

def ln(x: float) -> float:
    """
    Computes and approximation of natural log of x.
    :param x: The input of the ln function.
    :return: returns ln(x), natural log of x.
    """
    big_num: float = 1000000000000
    return big_num*(x**(1/big_num)-1)

# --- Activation Functions ---
def sigmoid(x: float) -> float:
    return 1 / (1 + exp(-x))


def tanh(x: float) -> float:
    ex1 = exp(x)
    ex2 = exp(-x)
    return (ex1-ex2)/(ex1+ex2)


def relu(x: float) -> float:
    return max(0.0, x)


def leaky_relu(x: float) -> float:
    return max(0.1 * x, x)


def elu(x: float) -> float:
    return x if x > 0 else exp(x) - 1


def selu(x: float) -> float:
    return 1.0507 * (1.67326 * x if x < 0 else x)


def swish(x: float) -> float:
    return x / (1 + exp(-x))


def mish(x: float) -> float:
    return x * tanh(log(1 + exp(x), EUCLIDS_NUMBER))


def gelu(x: float) -> float:
    return 0.5 * x * (1 + tanh(((2 / PI)**0.5) * (x + 0.044715 * x ** 3)))


def hard_sigmoid(x: float) -> float:
    return max(0.0, min(1.0, 0.2 * x + 0.5))

def linear(x: float) -> float:
    return x

def tanh_cutoff(x: float) -> float:
    # Check is x is defined in the domain of tanh. To avoid overflow.
    if x > 20:
        return 1
    elif x < -20:
        return -1
    else:
        return tanh(x)


def quadratic(x: float) -> float:
    return x ** 2


def abs_quadratic(x: float) -> float:
    return abs(x) * x  # keep the sign of x for usefulness.


def cubic(x: float) -> float:
    return x ** 3


def quartic(x: float) -> float:
    return x ** 4


def quintic(x: float) -> float:
    return x ** 5


def sakshamsLinearCutOff(x: float) -> float:
    diff = 0.5
    cut_off = 1
    if x > cut_off:
        return x * diff + (cut_off - diff)
    elif x < -cut_off:
        return x * diff - (cut_off - diff)
    return x


def softmax(outputs: list[float]) -> list[float]:
    return [exp(output) / sum([exp(output) for output in outputs]) for output in outputs]


def activation_function(x: float = 0.0, function: str = None) -> float:
    if function is None:
        return x
    if function == "sigmoid":
        return sigmoid(x)
    elif function == "tanh":
        return tanh(x)
    elif function == "relu":
        return relu(x)
    elif function == "leaky_relu":
        return leaky_relu(x)
    elif function == "elu":
        return elu(x)
    elif function == "selu":
        return selu(x)
    elif function == "swish":
        return swish(x)
    elif function == "mish":
        return mish(x)
    elif function == "gelu":
        return gelu(x)
    elif function == "hard_sigmoid":
        return hard_sigmoid(x)
    elif function == "exponential":
        return exp(x)
    elif function == "linear":
        return linear(x)
    elif function == "tanh":
        return tanh_cutoff(x)
    elif function == "quadratic":
        return quadratic(x)
    elif function == "abs_quadratic":
        return abs_quadratic(x)
    elif function == "cubic":
        return cubic(x)
    elif function == "quartic":
        return quartic(x)
    elif function == "quintic":
        return quintic(x)
    elif function == "SakshamsLinearCutOff":
        return sakshamsLinearCutOff(x)

    return x  # Linear by default if nothing works.
