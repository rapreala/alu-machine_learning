#!/usr/bin/env python3

"""Represents a Poisson distribution."""

class Poisson:
    """Represents a Poisson distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initializes the Poisson distribution.

        Args:
            data (list): A list of data
            to estimate the distribution.
            lambtha (float): The expected
            number of occurrences in a given time frame.

        Raises:
            ValueError: If lambtha is not positive
            or data is invalid.
            TypeError: If data is not a list.
        """

        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)  # Ensure lambtha is a float
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate lambtha from data
            self.lambtha = self._calculate_lambtha(data)

    def _calculate_lambtha(self, data):
        """Calculates the lambtha value from the given data."""
        lambtha_value = sum(data) / len(data)
        return lambtha_value

    def pmf(self, k):
        """Calculates the value of the PMF
        for a given number of 'successes'.

        Args:
            k (int or float): The number of 'successes'.

        Returns:
            float: The PMF value for k.
        """

        k = int(k)  # Ensure k is an integer

        if k < 0:
            return 0  # PMF is 0 for negative values of k

        e = 2.7182818285  # Provided approximation for e

        def factorial(n):
            """Calculates the factorial
            of a non-negative integer."""
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)  # Recursive calculation

        pmf_value = (e ** (-self.lambtha)) * (self.lambtha ** k) / factorial(k)
        return pmf_value
