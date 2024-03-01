#!/usr/bin/env python3
"""
this function performs convolution on images using multiple
kernels and various options.
"""

import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    Performs convolution on images using multiple kernels.

    Args:
        images (numpy.ndarray): Input images with shape (m, h, w, c).
        kernels (numpy.ndarray): Convolution kernels
        with shape (kh, kw, c, nc).
        padding (tuple or str): Padding option for the convolution.
        stride (tuple): Stride for the convolution operation.

    Returns:
        numpy.ndarray: Convolved images.
    """
    m, h, w, c = images.shape
    kh, kw, _, nc = kernels.shape
    sh, sw = stride

    if padding == 'valid':
        ph, pw = 0, 0
    elif padding == 'same':
        ph = ((((h - 1) * sh) + kh - h) // 2) + 1
        pw = ((((w - 1) * sw) + kw - w) // 2) + 1
    else:
        ph, pw = padding

    padded_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                           'constant')

    h_res = (h - kh + 2 * ph) // sh + 1
    w_res = (w - kw + 2 * pw) // sw + 1
    convolved_images = np.zeros((m, h_res, w_res, nc))

    for i in range(h_res):
        for j in range(w_res):
            for k in range(nc):
                convolved_images[:, i, j, k] = np.sum(
                    padded_images[:, i*sh:i*sh + kh, j*sw:j*sw + kw,
                                  :] * kernels[:, :, :, k], axis=(1, 2, 3))

    return convolved_images
