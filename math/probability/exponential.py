#!/usr/bin/env python3


"""Represents an exponential distribution."""


class Exponential:
    """Represents an exponential distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initializes the exponential distribution.

        Args:
            data (list): A list of data
            to estimate the distribution.
            lambtha (float): The expected number of
            occurrences in a given time frame.

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
