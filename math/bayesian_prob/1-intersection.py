#!/usr/bin/env python3
"""1-intersection.py"""


import numpy as np


def intersection(x, n, P, Pr):
        """
        Calculates the intersection of observing x side effects in n patients
        with various hypothetical probabilities (P) and prior beliefs (Pr).

        Args:
            x: Number of patients with severe side effects (int, non-negative).
            n: Total number of patients observed (positive integer).
            P: A 1D NumPy array of hypothetical probabilities (0 <= P <= 1).
            Pr: A 1D NumPy array of prior beliefs about P (same shape as P, 0 <= Pr <= 1, sum(Pr) = 1).

        Returns:
            A 1D NumPy array containing the intersection for each probability in P.

        Raises:
            ValueError:
                - If n is not a positive integer.
                - If x is not a non-negative integer.
                - If x is greater than n.
                - If any value in P or Pr is not between 0 and 1 (inclusive).
                - If Pr does not sum to 1.
            TypeError:
                - If P is not a 1D numpy.ndarray.
                - If Pr is not a 1D numpy.ndarray with the same shape as P.
        """

    # Validate input types and values
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a positive integer")
        error = "x must be an integer that is greater than or equal to 0"
        if not isinstance(x, int) or x < 0:
            raise ValueError(error)
        if x > n:
            raise ValueError("x cannot be greater than n")
        if not isinstance(P, np.ndarray) or len(P.shape) != 1:
            raise TypeError("P must be a 1D numpy.ndarray")
        if np.any(P < 0) or np.any(P > 1):
            raise ValueError("All values in P must be in the range [0, 1]")

        # Check if Pr sums to 1 (almost equal with a small tolerance)
        if not np.isclose(np.sum(Pr), 1, atol=1e-5):
            raise ValueError("Pr must sum to 1")

        # Intersection (posterior proportional to likelihood * prior)
        intersection_values = likelihood(x, n, P) * Pr

        return intersection_values
