#!/usr/bin/env python3
"""
    class MultiNormal that represents
    a Multivariate Normal distribution:
"""


import numpy as np
import sys  # Import for printing to standard error


class MultiNormal:
    """
    Represents a Multivariate Normal distribution.
    """

    def __init__(self, data):
        """
        Initializes a MultiNormal object.

        Args:
            data: A 2D numpy.ndarray of shape (d, n) containing the data set.

        Raises:
            TypeError: If data is not a 2D numpy.ndarray.
            ValueError: If data contains less than 2 data points.
        """

        if type(data) is not np.ndarray or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.data = data
        mean = np.mean(data, axis=1, keepdims=True)
        self.mean = mean
        cov = np.matmul(data - mean, data.T - mean.T) / (n - 1)
        self.cov = cov
