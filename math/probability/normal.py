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

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value.

        Args:
            x (float): The x-value.

        Returns:
            float: The PDF value for x.
        """

        e = 2.7182818285  # Approximate value of e
        pi = 3.1415926535  # Approximate value of pi

        # Calculate the z-score
        z = self.z_score(x)

        # Calculate the PDF using the formula
        pdf_value = (1 / (self.stddev * (2 * pi) ** 0.5)) * e ** (-0.5 * z**2)
        return pdf_value

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value.

        Args:
            x (float): The x-value.

        Returns:
            float: The CDF value for x.
        """

        # Approximate the CDF using numerical integration of the PDF
        dx = 0.0001  # Adjust step size for better precision
        cdf_value = 0
        # Integrate from negative infinity to x (using a large negative value)
        for i in range(int(-1000 * self.stddev), int(x / dx)):
            xi = i * dx
            pdf_value = self.pdf(xi)
            cdf_value += pdf_value * dx

        return cdf_value
