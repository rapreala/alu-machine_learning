#!/usr/bin/env python3
"""
this function performs convolutions on grayscale images.
"""

import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs convolutions on grayscale images.

    Args:
        images: A NumPy array with shape (m, h, w) containing grayscale images.
        kernel: A NumPy array with shape (kh, kw) containing the convolution
        kernel.

    Returns:
        A NumPy array with shape (m, output_h, output_w) containing
        the convolved images.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    output_h = h - kh + 1
    output_w = w - kw + 1
    convolved_images = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            convolved_images[:, i, j] = np.sum(
                images[:, i:i + kh, j:j + kw] * kernel, axis=(1, 2))

    return convolved_images
