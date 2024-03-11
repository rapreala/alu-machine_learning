#!/usr/bin/env python3
"""0-likelihood.py"""


import numpy as np


def likelihood(x, n, P):
    """
    Calculates the likelihood of observing x side effects in n patients
    given various hypothetical probabilities (P) of developing side effects.

    Args:
        x: Number of patients with severe side effects (int, non-negative).
        n: Total number of patients observed (positive integer).
        P: A 1D NumPy array of hypothetical probabilities (0 <= P <= 1).

    Returns:
        A 1D NumPy array containing the likelihood for each probability in P.

    Raises:
        ValueError:
            - If n is not a positive integer.
            - If x is not a non-negative integer.
            - If x is greater than n.
            - If any value in P is not between 0 and 1 (inclusive).
    """

    # Validate input types and values
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    # Calculate binomial coefficient (n choose x)
    coeff = np.math.factorial(n) / (np.math.factorial(x) * np.math.factorial(n - x))

    # Calculate likelihood for each probability in P
    likelihood_values = coeff * (P**x) * ((1 - P)**(n - x))

    return likelihood_values
