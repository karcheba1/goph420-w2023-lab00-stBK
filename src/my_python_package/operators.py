import numpy as np


def add(x, y):
    """Add two numbers or arrays.

    Parameters
    ----------
    x : int or float or array_like
        The first number to add.
    y : int or float or array_like
        The second number to add.

    Returns
    -------
    int or float or array_like
        The sum of x and y.
    """
    return x + y


def multiply(x, y):
    """Multiply two numbers or arrays.

    Parameters
    ----------
    x : int or float or array_like
        The first number to multiply.
    y : int or float or array_like
        The second number to multiply.

    Returns
    -------
    int or float or array_like
        The (element-wise) product of x and y.
    """
    return x * y
