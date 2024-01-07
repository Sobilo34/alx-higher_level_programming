#!/usr/bin/python3

"""This module contains a function that multiplies two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies two matrixes and return the output
    """

    return (np.matmul(m_a, m_b))
