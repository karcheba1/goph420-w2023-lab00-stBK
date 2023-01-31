import numpy as np

def global_to_local(z, z_e):
    """Converts global coordinate to local (element) coordinate.

    Parameters
    ----------
    z : float
        The global coordinate to convert to local coordinate
    z_e : array_like, shape = (2,)
        Nodal coordinates of the element

    Returns
    -------
    float
        The local coordinate
    """
    return (z - z_e[0]) / (z_e[1] - z_e[0])


def shape_matrix(s):
    """Calculate the shape function matrix for 1d linear interpolation.

    Parameters
    ----------
    s : float
        The local coordinate in the element

    Returns
    -------
    numpy.ndarray, shape = (1, 2)
        The shape function matrix
    """
    return np.array([[(1 - s), s]])


def gradient_matrix(s, dz):
    """Calculate the gradient matrix for 1d linear interpolation.

    Parameters
    ----------
    s : float
        The local coordinate in the element
    dz : float
        The scaling factor from global to local coordinates

    Returns
    -------
    numpy.ndarray, shape = (1, 2)
        The gradient matrix
    """
    return np.array([[-1, 1]]) / dz
