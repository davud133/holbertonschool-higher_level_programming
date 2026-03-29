#!/usr/bin/python3
"""Module that multiplies 2 matrices using NumPy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy"""
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        if "did not contain a loop with signature matching types" in str(e):
            raise ValueError("Scalar operands are not allowed, use '*' instead")
        raise
