#!/usr/bin/env python3
"""0-mean_cov.py"""


import numpy as np


def correlation(C):
    """
    Calculates the correlation matrix from a covariance matrix.

    Args:
        C: A 2D numpy.ndarray of shape (d, d) containing a covariance matrix.

    Returns:
        A numpy.ndarray of shape (d, d) containing the correlation matrix.

    Raises:
        TypeError: If C is not a numpy.ndarray.
        ValueError: If C does not have a square shape (d, d).
    """

    # Check if C is a numpy.ndarray
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    # Check if C has a square shape (d, d)
    if C.shape != C.shape[::-1]:
        raise ValueError("C must be a 2D square matrix")

    # Standard deviations (square root of diagonal elements)
    std_dev = np.sqrt(np.diag(C))

    # Expand std_dev to a 2D square matrix for element-wise division
    std_dev_mat = np.expand_dims(std_dev, axis=1) * np.expand_dims(std_dev, axis=0)

    # Avoid division by zero (replace diagonals with 1e-8)
    std_dev_mat[np.diag_indices(std_dev_mat.shape[0])] = 1e-8

    # Correlation matrix (covariance divided by element-wise standard deviations)
    correlation_matrix = C / std_dev_mat

    return correlation_matrix

# Example usage (assuming you saved the function in 1-correlation.py)
if __name__ == '__main__':
    import numpy as np
    correlation = __import__('1-correlation').correlation

    C = np.array([[36, -30, 15], [-30, 100, -20], [15, -20, 25]])
    Co = correlation(C)
    print(C)
    print(Co)
