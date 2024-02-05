#!/usr/bin/env python3


"""Represents a normal distribution."""


class Normal:
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
