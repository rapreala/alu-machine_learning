#!/usr/bin/env python3
"""
Module for performing valid convolution on grayscale images.
"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs valid convolution on grayscale images.

    Args:
        images: A NumPy array with shape (m, h, w) containing grayscale images.
        kernel: A NumPy array with shape (kh, kw) containing the convolution 
        kernel.

    Returns:
        A NumPy array with shape (m, output_h, output_w) containing 
        the convolved images.
    """

    # Calculate output dimensions (valid padding)
    output_h = images.shape[1] - kernel.shape[0] + 1
    output_w = images.shape[2] - kernel.shape[1] + 1

    # Initialize output array
    convolved_images = np.zeros((images.shape[0], output_h, output_w))

    # Iterate over each image
    for i in range(images.shape[0]):
        image = images[i]

        # Iterate over output image dimensions
        for y in range(output_h):
            for x in range(output_w):
                # Extract image patch for convolution
                image_patch = image[y:y+kernel.shape[0], x:x+kernel.shape[1]]

                # Perform element-wise multiplication and sum
                convolved_value = np.sum(image_patch * kernel)

                # Store the convolution result
                convolved_images[i, y, x] = convolved_value

    return convolved_images
