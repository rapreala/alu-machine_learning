#!/usr/bin/env python3
"""
    class MultiNormal that represents
    a Multivariate Normal distribution:
"""


import numpy as np


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

        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        num_data_points, num_features = data.shape
        if num_data_points < 2:
            raise ValueError("data must contain multiple data points")

        self.data = data

        # Calculate mean vector
        mean = np.mean(data, axis=1, keepdims=True)

        # Calculate unbiased covariance matrix
        centered_data = data - mean
        cov = np.matmul(centered_data, centered_data.T) / (num_data_points - 1)

        self.mean = mean
        self.cov = cov
