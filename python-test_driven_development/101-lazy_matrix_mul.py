#!/usr/bin/python3
"""Module that multiplies 2 matrices using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 matrices using NumPy."""
    if np.isscalar(m_a) or np.isscalar(m_b):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    return np.dot(m_a, m_b)
