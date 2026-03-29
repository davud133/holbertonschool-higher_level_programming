#!/usr/bin/python3
"""Module that multiplies 2 matrices using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy."""
    return np.dot(m_a, m_b)
