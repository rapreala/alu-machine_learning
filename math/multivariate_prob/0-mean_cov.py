#!/usr/bin/env python3
"""0-mean_cov.py"""


import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance of a data set.

    Args:
        X: A 2D numpy.ndarray of shape (n, d) containing the data set.

    Returns:
        A tuple containing two numpy.ndarrays:
            - mean: A numpy.ndarray of shape (1, d)
            containing the mean of the data set.
            - cov: A numpy.ndarray of shape (d, d)
            containing the covariance matrix of the data set.

    Raises:
        TypeError: If X is not a 2D numpy.ndarray.
        ValueError: If X contains less than 2 data points.
    """

    # Check if X is a 2D numpy.ndarray
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    # Check if X has at least 2 data points
    if X.shape[0] < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate the mean
    mean = np.mean(X, axis=0)  # Average across columns (data points)
    mean = mean.reshape(1, -1)  # Reshape mean to a 1D row vector

    # Calculate the covariance matrix (avoiding numpy.cov)
    centered_X = X - mean  # Center the data by subtracting the mean

    # Covariance formula
    cov = np.dot(centered_X.T, centered_X) / (X.shape[0] - 1)

    return mean, cov


# Example usage (assuming you saved the function in 0-mean_cov.py)
if __name__ == '__main__':
    import numpy as np
    mean_cov = __import__('0-mean_cov').mean_cov

    np.random.seed(0)
    X = np.random.multivariate_normal([12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000)
    mean, cov = mean_cov(X)
    print(mean)
    print(cov)
