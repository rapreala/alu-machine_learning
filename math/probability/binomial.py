#!/usr/bin/env python3


"""Represents an exponential distribution."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initializes the binomial distribution.

        Args:
            data (list): A list of data to estimate the distribution.
            n (int): The number of Bernoulli trials.
            p (float): The probability of a "success".

        Raises:
            ValueError: If n is not positive, p is not a valid probability,
                       or data is invalid.
            TypeError: If data is not a list.
        """

        if data is None:
            # Use given n and p
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not 0 < p < 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = p
        else:
            # Calculate n and p from data
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate p first
            self.p = sum(1 for x in data if x == 1) / len(data)

            # Calculate n, rounding to nearest integer
            self.n = round(sum(data) / self.p)

            # Recalculate p for consistency
            self.p = sum(1 for x in data if x == 1) / len(data)
