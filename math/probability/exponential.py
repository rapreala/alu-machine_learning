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

    def _calculate_lambtha(self, data):
        """Calculates the lambtha value from the given data."""
        total = sum(data)  # Calculate the sum of the data manually
        count = len(data)  # Calculate the number of data points
        # Estimate lambtha using the formula for mean
        lambtha_value = count / total
        return lambtha_value

    def pdf(self, x):
        """Calculates the value of the PDF for a given time period.

        Args:
            x (float): The time period.

        Returns:
            float: The PDF value for x.
        """

        if x < 0:
            return 0  # PDF is 0 for negative values of x

        e = 2.7182818285  # Approximate value of e
        # PDF formula using manual exponentiation
        pdf_value = self.lambtha * (e ** (-self.lambtha * x))
        return pdf_value
