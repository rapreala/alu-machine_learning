#!/usr/bin/env python3


"""Represents a normal distribution."""


class Normal:
    """Represents a normal distribution."""
    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes the normal distribution.

        Args:
            data (list): A list of data to estimate the distribution.
            mean (float): The mean of the distribution.
            stddev (float): The standard deviation of the distribution.

        Raises:
            ValueError: If stddev is not positive or data is invalid.
            TypeError: If data is not a list.
        """

        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)  # Ensure mean is a float
            self.stddev = float(stddev)  # Ensure stddev is a float
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate mean and standard deviation from data
            self.mean = float(sum(data) / len(data))
            # Note: Manual calculation of stddev for adherence to constraints
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)
    
    def z_score(self, x):
        """Calculates the z-score of a given x-value.

        Args:
            x (float): The x-value.

        Returns:
            float: The z-score of x.
        """

        z_score = (x - self.mean) / self.stddev
        return z_score

    def x_value(self, z):
        """Calculates the x-value of a given z-score.

        Args:
            z (float): The z-score.

        Returns:
            float: The x-value of z.
        """

        x_value = self.mean + z * self.stddev
        return x_value
